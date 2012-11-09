from django.core.exceptions import PermissionDenied
from django.db import connection, transaction
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response


from search398.simplesearch.models import User, PreviousSearch


import cgi
import random
import urlparse


csrf_counter = random.randint(1000, 2000000000)

def attack(request):
	return render_to_response('simplesearch/attack.html')

def _query_db_by_username_secure(username, password):
  try:
    return User.objects.get(username=username, password=password)
  except User.DoesNotExist:
    return None


def _query_db_by_username_naive(username, password):
  cursor = connection.cursor()

  q = ('SELECT * FROM simplesearch_user WHERE username=\'%s\' AND password=\'%s\';'
       % (username, password))
  cursor.execute(q)
  # We would never add this commit in real code! Force vulnerability.
  # (Of course, we also wouldn't write our own SQL in real code, we'd
  # do _query_db_by_username_secure instead.)
  transaction.commit_unless_managed()

  result = cursor.fetchone()
  if result is None:
    return None
  (id, username, password) = result
  return User(pk=id, username=username, password=password)
  

def _query_db_by_username_escape_quotes(username, password):
  def escape_quotes(s):
    return s.replace('\'', '\'\'')
  return _query_db_by_username_naive(escape_quotes(username),
                                     escape_quotes(password))


def _check_login_cookie(cookie_content):
  if cookie_content is None:
    return None
  # Need cgi in python2.5 because parse_qs is missing from urlparse.
  d = cgi.parse_qs(cookie_content)
  try:
    return User.objects.get(username=d['username'][0])
  except KeyError:
    return None
  except User.DoesNotExist:
    return None


def index(request):
  user = _check_login_cookie(request.COOKIES.get('login'))
  csrfdefense = int(request.GET.get('csrfdefense', '0'))

  if user is None and csrfdefense == 1:
    global csrf_counter
    csrf_counter += 1

  return render_to_response(
      'simplesearch/index.html',
      {'user': user,
       'csrfdefense': csrfdefense,
       'csrf_counter': csrf_counter,
       'searches': _get_searches(user)})


def _get_searches(db_user):
  return PreviousSearch.objects.filter(user=db_user).order_by('-search_time')[:10]


def search(request):
  search_term = request.GET.get('q', '')
  xssdefense = int(request.GET.get('xssdefense', '0'))
  csrfdefense = int(request.GET.get('csrfdefense', '0'))
  if xssdefense < 0:
    raise Exception('invalid XSS defense %d' % xssdefense)

  logged_in_user = _check_login_cookie(request.COOKIES.get('login'))
  searches = None
  if logged_in_user is not None:
    ps = PreviousSearch(user=logged_in_user, term=search_term)
    ps.save()
    searches = _get_searches(logged_in_user)
  elif csrfdefense == 1:
    global csrf_counter
    csrf_counter += 1

  return render_to_response('simplesearch/search.html',
                            {'term': search_term,  'user': logged_in_user,
                             'searches': searches, 'xssdefense': xssdefense,
                             'csrfdefense': csrfdefense, 'csrf_counter': csrf_counter})


def _validate_referer(request):
  referer = request.META.get('HTTP_REFERER', '')
  referer_netloc = urlparse.urlparse(referer).netloc
  return (not referer_netloc) or referer_netloc == '127.0.0.1:8000'


def _render_login_sidebar(request, failed=False, reset=False):
  global csrf_counter
  csrfdefense = int(request.GET.get('csrfdefense', '0'))
  csrf_counter += 1
  context = {'failed': failed,
             'reset': reset,
             'csrf_counter': csrf_counter,
             'csrfdefense': csrfdefense}
  return render_to_response('simplesearch/login.html', context)
  

def login(request):
  global csrf_counter
  user = request.POST['user']
  password = request.POST['password']
  action = request.POST['login_action']
  secretanswer = request.POST.get('secretanswer')
  sqlfilter = int(request.POST['sqlfilter'])
  sent_counter = int(request.POST.get('csrfcounter', -1))
  csrfdefense = int(request.GET['csrfdefense'])

  failed = False
  should_set_login_cookie = False
  reset = False

  if sqlfilter == 0:
    db_user = _query_db_by_username_naive(user, password)
  elif sqlfilter == 1:
    db_user = _query_db_by_username_escape_quotes(user, password)
  else:
    raise Exception('Invalid SQL difficulty setting %d' % sqlfilter)

  if action == 'login':
    if db_user is None:
      failed = True
    else:
      if csrfdefense == 1 and not 0 <= (csrf_counter - sent_counter) < 10:
        raise PermissionDenied()
      elif csrfdefense == 2:
        if not _validate_referer(request):
          raise PermissionDenied()

      should_set_login_cookie = True
  elif action == 'register':
    if db_user is not None:
      failed = True
    else:
      db_user = User(username=user, password=password)
      db_user.save()
      should_set_login_cookie = True
  elif action == 'reset':
    if db_user is None:
      failed = True
    else:
      reset = True

  if failed:
    response = _render_login_sidebar(request, failed=failed, reset=reset)
  else:
    context = {'searches': _get_searches(db_user),
               'user': db_user}
    response = render_to_response('simplesearch/history.html', context)

  if should_set_login_cookie:
    response.set_cookie('login', 'username=%s' % db_user)
  return response


def logout(request):
  csrfdefense = int(request.GET.get('csrfdefense', '0'))
  if csrfdefense == 2 and not _validate_referer(request):
    raise PermissionDenied()

  response = _render_login_sidebar(request)
  response.delete_cookie('login')
  return response

from django import template


import re
import urllib


register = template.Library()


# Cut removes all occurrences of a string from a value.
cut = template.defaultfilters.cut


RE = re.compile('script|<img|<body|<style|<meta', re.I)


RE2 = re.compile('script|<img|<body|<style|<meta|<embed', re.I)


def remove_opening_script(value):
  return cut(value, '<script')


def remove_js_punctuation(value):
  return cut(cut(cut(value, '\''), '"'), ';')


def remove_several_tags(value):
  return RE.sub('', value)


def remove_more_tags(value):
  return RE2.sub('', value)


def extra_defense(value, arg):
  url = 'http://fafner.eecs.umich.edu/extra_defense'
  data = [('q', value), ('defense', arg)]
  return urllib.urlopen(url, data).read()


register.filter('remove_opening_script', remove_opening_script)
register.filter('remove_js_punctuation', remove_js_punctuation)
register.filter('remove_several_tags', remove_several_tags)
register.filter('remove_more_tags', remove_more_tags)
register.filter('extra_defense', extra_defense)

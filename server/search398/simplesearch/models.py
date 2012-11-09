from django.db import models

class User(models.Model):
  username = models.CharField(max_length=8)
  password = models.CharField(max_length=24)
  def __unicode__(self):
    return self.username

class PreviousSearch(models.Model):
  user = models.ForeignKey(User)
  term = models.CharField(max_length=200)
  search_time = models.DateTimeField(auto_now=True)
  def __unicode__(self):
    return self.term

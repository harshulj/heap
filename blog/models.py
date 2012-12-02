from django.db import models
from django.contrib.auth.models  import User

class Collection(models.Model):
    """
    Collection is model for a collection of entries.
    """
    name = models.CharField(max_length=50, verbose_name="Collection Name")
    link = models.SlugField(max_length=60)
    created_on = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name='collections')

    class Meta():
        verbose_name_plural = "collections"

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    """
    This models the Entry a user creates.
    """
    text = models.TextField(verbose_name="Entry Text")
    title = models.CharField(max_length=100, verbose_name="Entry Title")
    link = models.SlugField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, related_name='entries')
    author = models.ForeignKey(User, related_name='entries')

    class Meta():
        verbose_name_plural = "entries"

    def __unicode__(self):
        return self.title

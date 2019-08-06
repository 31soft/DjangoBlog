from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    context = models.TextField(max_length=10000)
    datetime = models.DateTimeField(u'Дата публикации')  # дата публикации
    public = models.BooleanField(default=True)

    #datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    #content = models.TextField() # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
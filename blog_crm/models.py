from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


# Removing Post Category should be dynamically added to DB, using a list to fasten things up

POST_CATEGORY = (
    ('entertainment', 'Entertainment'),
    ('housing', 'Housing'),
    ('house_owner', 'House Ownder'),

)


class NewPost(models.Model):
    category = models.CharField(choices=POST_CATEGORY, max_length=20)
    title = models.CharField(max_length=70)
    image = models.ImageField()
    content = RichTextField()
    publish = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        permissions = (
            ('approve_post', 'Can approve post'),
        )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):

        self.slug = slugify(self.title)
        super(NewPost, self).save(*args, **kwargs)

    def __str__(self):

        return self.title

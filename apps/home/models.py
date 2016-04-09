from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models

from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    """
    Article Category model....
    """
    category_name = models.CharField(_('Category'), max_length=255)

    def __unicode__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Article category..'
        verbose_name_plural = 'Article categories.'


class Article(models.Model):
    """
    Article model....
    """
    name = models.CharField(_('Name'), max_length=255)
    author = models.CharField(_('Author'), max_length=200)
    publish_date = models.DateField(_('Published date'), max_length=255)
    category = models.ForeignKey(Category)
    image = models.ImageField(_('Hero image..'), upload_to='heros/')
    addtional_image = models.ImageField(_('Additional image'),upload_to='additional/', null=True, blank=True)
    content = RichTextField()

    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(84, 47)],
                                      format='JPEG',
                                      options={'quality': 60})

    addtional_image_thumbnail = ImageSpecField(source='addtional_image',
                                      processors=[ResizeToFill(753, 424)],
                                      format='JPEG',
                                      options={'quality': 60})


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Article..'
        verbose_name_plural = 'Articles..'
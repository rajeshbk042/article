from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField


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

    slider_image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(176, 134)],
                                      format='JPEG',
                                      options={'quality': 60})

    addtional_image_thumbnail = ImageSpecField(source='addtional_image',
                                      processors=[ResizeToFill(753, 424)],
                                      format='JPEG',
                                      options={'quality': 60})

    slug = AutoSlugField(populate_from='name')


    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Article..'
        verbose_name_plural = 'Articles..'
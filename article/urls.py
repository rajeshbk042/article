from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from apps.home.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ArticleListView.as_view(), name='home'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
)


urlpatterns += patterns('',
                        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
                        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
                        )
urlpatterns += staticfiles_urlpatterns()
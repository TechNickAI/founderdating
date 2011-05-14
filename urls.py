from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from os import path

admin.autodiscover()

urlpatterns = patterns('',

    # Static content
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': path.join(settings.ROOT_PATH, 'profiles', 'static')}),
    (r'^(favicon.ico)', 'django.views.static.serve',
        {'document_root' : path.join(settings.ROOT_PATH, 'profiles', 'static', 'img')}),
    (r'^(robots.txt)', 'django.views.static.serve',
        {'document_root' : path.join(settings.ROOT_PATH, 'profiles', 'static')}),

    # basic account creation
    (r'^profiles/', include('userena.urls')),
    (r'^accounts/', include('userena.urls')),

    # Application process
    (r'^attend', 'fd.profiles.views.attend'),

    # List upcoming events
    (r'^upcoming', 'fd.profiles.views.events'),

    # social auth for linkedin hookup
    url(r'', include('social_auth.urls')),

    # django admin
    url(r'^internal_admin/', include(admin.site.urls)),
    (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),

    # Zinnia (blog)
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    # django cms
    url(r'^', include('cms.urls')),

)
urlpatterns += staticfiles_urlpatterns()


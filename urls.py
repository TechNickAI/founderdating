from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fd.views.home', name='home'),
    # url(r'^fd/', include('fd.foo.urls')),
    
    # basic account creation
    (r'^profiles/', include('userena.urls')),
    (r'^accounts/', include('userena.urls')),

    # Application process
    (r'^attend', 'fd.profiles.views.attend'),

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


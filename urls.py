from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fd.views.home', name='home'),
    # url(r'^fd/', include('fd.foo.urls')),
    
    (r'^profiles/', include('userena.urls')),
    (r'^accounts/', include('userena.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^internal_admin/', include(admin.site.urls)),

)
urlpatterns += staticfiles_urlpatterns()

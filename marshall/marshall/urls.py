from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'web.views.index', name='home'),
                       url(r'^contact$', 'web.views.contact', name='contact'),
)

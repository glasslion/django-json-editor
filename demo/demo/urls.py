from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'demo.views.demo_home', name='demo_home'),
    # url(r'^blog/', include('blog.urls')),

)

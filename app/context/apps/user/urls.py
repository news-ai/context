# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import RedirectView

urlpatterns = patterns('context.apps.user.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^register/$', 'register', name='register'),
                       url(r'^login/$', 'user_login', name='login'),
                       url(r'^logout/$', 'user_logout', name='logout'),
                       )

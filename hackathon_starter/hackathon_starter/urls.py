from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ('^activity/', include('actstream.urls')),
    # url(r'^openid/(.*)', SessionConsumer()),
)

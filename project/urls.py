from django.conf.urls import patterns, include, url
from django.contrib import admin
from calc import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(\d+)\+(\d+)$', views.suma, name="suma"),
    url(r'^(\d+)\-(\d+)$', views.resta, name="resta"),
    url(r'^(\d+)\*(\d+)$', views.multiplicacion, name="multiplicacion"),
    url(r'^(\d+)/(\d+)$', views.division, name="division"),
)

from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from settings import STATIC_ROOT, MEDIA_ROOT
from home import views as home_views
from about import views as about_views
from activities import views as activities_views
from availability import views as availability_views
from prices import views as prices_views
from weather import views as weather_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    url(r'^$', home_views.get_index),
    url(r'^home/$', home_views.get_index, name="home"),
    url(r'^about/$', about_views.get_index, name="about"),
    url(r'^activities/$', activities_views.get_index, name="activities"),
    url(r'^prices/$', prices_views.get_index, name="prices"),
    url(r'^availability/$', availability_views.get_index, name="availability"),
    url(r'^weather/$', weather_views.get_index, name="weather"),


]

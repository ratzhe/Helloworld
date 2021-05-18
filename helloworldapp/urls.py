from django.contrib import admin
from django.urls import path, include
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', include('helloworldapp.urls')),
]
include
from django.urls import path
from . import views
urlpatterns = [
 path('', views.helloworld_views, name='helloworld_views'),
]

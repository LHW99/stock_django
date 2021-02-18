from django.urls import path
from . import views
from django.urls import include
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# home page
urlpatterns = [
  path('', views.index, name='index'),
  path('top50gain/', views.top50gain, name='top50gain'),
  path('top50loss/', views.top50loss, name='top50loss'),
  path('top50pe/', views.top50pe, name='top50pe'),
  path('all/', views.all, name='all'),
  path('compare/', views.compare, name='compare'),
]
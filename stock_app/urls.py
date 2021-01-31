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
  path('top50/', views.top50, name='top50'),
  path('watchlist/', views.watchlist, name='watchlist')
]
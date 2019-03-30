from django.conf.urls import include, url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from django.contrib import admin
from bills import views
from django.urls import path, include

urlpatterns = [
  path('', views.BillAPIListView.as_view()),
  path('bills/<int:id>', views.BillAPIView.as_view()),
  path('bills/', views.BillAPIListView.as_view()),

  path('category/<int:id>', views.CategoryAPIView.as_view()),
  path('category/', views.CategoryAPIListView.as_view()),

]

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('faqs/', views.FaqsView.as_view(), name='faqs'),
    path('report/', views.ReportsView.as_view(), name='report'),
]
from django.contrib import admin
from django.urls import path,include
from notes import views

urlpatterns = [
   path('',views.index),
   path('notes/',views.notes),
   path('profile/',views.profile),
   path('about/',views.about),
   path('contact/',views.contact),
]

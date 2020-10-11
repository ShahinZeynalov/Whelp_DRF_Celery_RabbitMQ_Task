from django.contrib import admin
from django.urls import path
from .views import celery_view

urlpatterns = [
   path('celerytask/', celery_view),
]
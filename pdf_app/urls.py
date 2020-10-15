from django.contrib import admin
from django.urls import path
from .views.views import  (
   CreateDocumentAPIView, RetrieveDocumentRetrieveAPIView
)

from rest_framework import routers
from .views.haystack_views import DocumentSearchView
router = routers.DefaultRouter()
router.register('search', DocumentSearchView, basename='search')

urlpatterns = [
   path('create/', CreateDocumentAPIView.as_view()),
   path('check/<int:pk>/', RetrieveDocumentRetrieveAPIView.as_view()),
] + router.urls
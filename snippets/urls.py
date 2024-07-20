from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from snippets.views import api_root, SnippetViewSet, UserViewSet


# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippet')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', views.api_root),
    path('', include(router.urls)),
]
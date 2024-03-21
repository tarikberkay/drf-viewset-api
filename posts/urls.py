from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('authors', AuthorViewSet)
router.register('tags', TagViewSet)

urlpatterns =[
    path('', include(router.urls))
]

from django.urls import path, include
from .views import FolderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('folder', FolderViewSet, basename='folder')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]
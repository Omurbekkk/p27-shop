from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryListCreateAPIView, CategoryDestroyAPIView

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDestroyAPIView.as_view()),
]


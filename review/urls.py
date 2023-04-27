from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, FavouriteViewSet, AddRatingAPIView


router = DefaultRouter()
router.register("comments", CommentViewSet)
router.register("favourites", FavouriteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("rating/", AddRatingAPIView.as_view()),
]


from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    # apiviewのセットの仕方
    path('hello-view/', views.HelloApiView.as_view()),
    # viewsetのセットの仕方
    path('', include(router.urls))

]
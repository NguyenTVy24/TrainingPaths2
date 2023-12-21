from django.urls import path
from .views import User_view 
from .views import Assets_views

urlpatterns = [
    path('user', User_view.getData),
    path ('user/create', User_view.add),
    path ('user/read/<str:pk>', User_view.getId),
    path ('user/update/<str:pk>', User_view.update),
    path ('user/delete/<str:pk>', User_view.delete),
    path('assets/', Assets_views.getData),
    path ('assets/create', Assets_views.add),
    path ('assets/read/<str:pk>', Assets_views.getId),
    path ('assets/update/<str:pk>', Assets_views.update),
    path ('assets/delete/<str:pk>', Assets_views.delete),
    path('user/<str:pk>/assets/', Assets_views.getFollowUser),
]
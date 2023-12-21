from django.urls import path
from . import views

urlpatterns = [
    path('user', views.getDataUser),
    path ('user/create', views.addUser),
    path ('user/read/<str:pk>', views.getUser),
    path ('user/update/<str:pk>', views.updateUser),
    path ('user/delete/<str:pk>', views.deleteUser),
    path('assets/', views.getDataAssets),
    path ('assets/create', views.addAssets),
    path ('assets/read/<str:pk>', views.getAssets),
    path ('assets/update/<str:pk>', views.updateAssets),
    path ('assets/delete/<str:pk>', views.deleteAssets),
    path('user/<str:pk>/assets/', views.getAssetsUser),
]
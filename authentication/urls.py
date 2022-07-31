from authentication import views
from django.urls import path

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name = 'register'),
    path('logins', views.LoginAPIView.as_view(), name = 'login'),
    path('user', views.AuthUserAPIView.as_view(), name = 'user')   
]
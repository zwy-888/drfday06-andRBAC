from django.urls import path

from api import views

urlpatterns = [
    path('user/', views.UserAPIView.as_view())
]

from django.urls import path,include
from accounts import views as UseViews

urlpatterns = [
    path('register/', UseViews.RegisterUserView.as_view()),
    
    ]
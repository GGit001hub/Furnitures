from django.urls import path
from .views import *

urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('profile/',UserProfileView.as_view()),
    path('changepass/',UserPasswordChangeView.as_view()),
    path('send-reset-password-email/',SendResetPasswordEmailView.as_view()),
    path('reset-password/<uid>/<token>/',UserResetPassworView.as_view()),
]

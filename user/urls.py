from django.urls import path, include
from user import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("signup/", views.UserView.as_view(), name="user_view"),
    path("profile/", views.ProfileView.as_view(), name="profile_view"),
    path("api/token/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path('kakao/login/', views.kakao_login, name='kakao'),
    path('kakao/callback/', views.kakao_callback, name='kakao'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao'),
]
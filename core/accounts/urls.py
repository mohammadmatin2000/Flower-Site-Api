from django.urls import path
from .views import RegisterViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# ======================================================================================================================
urlpatterns = [
    path('register/',RegisterViews.as_view(),name='register'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('logout/',TokenRefreshView.as_view(),name='logout'),

]
# ======================================================================================================================
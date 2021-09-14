from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 
from core import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
    path('api-auth/', include('rest_framework.urls')),
]
from django.urls import path, include
from Authentication.views import login_user, register_user, logout_user

app_name = 'Authentication'

urlpatterns = [
    path('login/<str:status>/', login_user, name = 'login-user'),
    path('register/<str:status>', register_user, name = 'register-user'),
    path('logout/', logout_user, name = 'logout-user')
]
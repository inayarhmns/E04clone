from django.urls import path, include
from Authentication.views import login_user, register_user, logout_user, get_pengunjung, login_flutter

app_name = 'Authentication'

urlpatterns = [
    path('login/<str:status>/', login_user, name = 'login-user'),
    path('register/<str:status>', register_user, name = 'register-user'),
    path('logout/', logout_user, name = 'logout-user'),
    path('json/', get_pengunjung, name = 'json'),
    path('login_flutter', login_flutter, name = 'login_flutter'),
]
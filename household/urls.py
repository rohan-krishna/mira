from django.urls import path
from . import views

app_name='household'

urlpatterns=[
    path('user-login',views.user_login, name='user_login'),
    path('user-logout',views.user_logout, name='user_logout'),
]
from django.urls import path , include
from courage.views import home, login_user,logout_view,register_user

urlpatterns = [
    path('', home, name="home"),
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_view, name="logout")
]
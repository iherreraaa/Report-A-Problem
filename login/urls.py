from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('register/',views.registerPage),
    path('login/', views.loginPage),
    path('logout/', views.logoutUser, name='logout'),

    path('',views.home, name="home")
]
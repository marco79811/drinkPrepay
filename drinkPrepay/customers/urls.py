from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy
from customers.views import profile,register

app_name='customers'


urlpatterns = [

path('login/',
    LoginView.as_view
    (template_name='customers/login.html', 
     redirect_authenticated_user=True
    ),
    name='login',
    ),

path('logout/',
LogoutView.as_view(

),
name='logout'
),

path("profile/",profile, name="profile"),
path('register/',register,name='register'),
    
]
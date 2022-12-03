from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy

from redeem.views import shopcart

app_name='redeem'


urlpatterns = [



path('shopcart/',shopcart,name='shopcart'),
    
]
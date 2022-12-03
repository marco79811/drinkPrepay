from django.urls import path

from cafe.views import coffee_list

app_name='cafe'


urlpatterns = [



path("coffee-list/",coffee_list, name="coffee_list"),

    
]
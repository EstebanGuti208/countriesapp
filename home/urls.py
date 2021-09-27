from django.urls import path
from home import views

urlpatterns = [
    path(route = '', 
    view=views.get_country, 
    name='country'
    ),
]
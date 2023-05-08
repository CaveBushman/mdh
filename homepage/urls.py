from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path ('', views.index, name = 'homepage'),
    path ('malina', views.malina, name = 'malina'),
    path ('premiot', views.premiot, name = 'premiot')
]
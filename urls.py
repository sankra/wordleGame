from django.urls import path
from . import views

#urlpatterns = [
#    path('', views.home, name='home'),  # Home page
#]


urlpatterns = [
    path('', views.home, name='home'),  # Existing home page
    path('game/', views.game, name='game'),  # New page
]
from django.urls import path
from .views import game_view, reset_game

urlpatterns = [
    path("", game_view, name="home"),
    path("view", game_view, name="game"),
    path("reset/", reset_game, name="resetgame")
]

from django.shortcuts import render
from rest_framework import viewsets,  permissions
from game.serializers import GameSerializer
from game.models import Partida

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):

    queryset = Partida.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

        
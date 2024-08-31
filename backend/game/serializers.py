from game.models import Partida

from rest_framework import serializers

class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Partida
        fields = [
            'anfitiron',
            'estado'
        ]

    #def post(request):
    #    pass
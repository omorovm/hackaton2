from rest_framework import serializers
from .models import Favorite


class FavoriteSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    dish = serializers.ReadOnlyField(source='dish.name')

    class Meta:
        fields = '__all__'
        model = Favorite
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        return repr['dish']
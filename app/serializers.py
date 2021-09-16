from rest_framework import serializers 
from app.models import Tutorial
 
 
class AppSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')
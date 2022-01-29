from rest_framework import serializers
from .models import Blogpost
# Serializers define the API representation.
class BlogpostSerializer(serializers.ModelSerializer): #this serializer for every api
    class Meta:
        model = Blogpost
        fields = '__all__'
        lookup_field = 'slug'
 
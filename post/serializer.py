from rest_framework import serializers
from . models import Article

class ArtcileSerializer(serializers.Serializers):
    title = serializers.CharField(max_length=128)
    author = serializers.CharField(max_length=128)
    email = serializers.EmailField(max_length=128)
    time = serializers.DateTimeField()
    #slug = serializers.SlugField()
    text = serializers.TextField()
    date = serializers.DateTimeField()

    # Function to convert into json format
    
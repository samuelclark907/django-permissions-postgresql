from rest_framework import generics
from .serializer import DinoSerializer
from .models import Dino
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Dino.objects.all()
    serializer_class = DinoSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dino.objects.all()
    serializer_class = DinoSerializer

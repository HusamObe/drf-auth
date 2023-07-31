from django.shortcuts import render
from .models import Comic
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ComicSerializer
from .permissions import OwnerOnly


class ComicListView(ListCreateAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
    

class ComicDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
    permission_classes = [OwnerOnly]
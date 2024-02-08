from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
# Create your views here.

class CreateView(CreateAPIView):
    
    serializer_class = NoteSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data)
class ListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    
class DeleteView(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)


from .models import Book
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from rest_framework import generics


# API's data list view and create data
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
# To see one API data by id
class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer





from library.serializer import BookSerializer, AuthorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.
@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)

    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)
    return Response(book_serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_author(request):
    author_serialiser =AuthorSerializer(data=request.data)

    if author_serialiser.is_valid():
        author_serialiser.save()
        return Response(author_serialiser.data, status=status.HTTP_201_CREATED)
    return Response(author_serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
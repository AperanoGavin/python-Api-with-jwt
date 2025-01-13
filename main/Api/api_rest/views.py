from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status 
from Api.models import Movie
from Api.api_rest.serializers import MovieSerializer


@api_view(['GET' , 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies =  Movie.objects.all()
        serializer = MovieSerializer(movies , many=True)
        return Response(serializer.data)
    else:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET' , 'PUT' , 'DELETE'])
def movie_details(request , pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data , status= status.HTTP_200_OK)
    elif request.method == 'PUT':
         movie = Movie.objects.get(pk=pk)
         serializer = MovieSerializer(movie ,data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data , status= status.HTTP_200_OK)
         return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MovieSerializer(data = request.data)
        movie.delete()
        return Response(status= status.HTTP_200_OK)

    
    
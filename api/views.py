from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer, CommentSerializer
from .models import Movie, Comment
import requests

# Create your views here.
"""@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Movie': '/movie/<str:name>',
        'Movie List': '/movie-list/'
    }

    return Response(api_urls)
"""

@api_view(['GET'])
def allMovie(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewMovie(request, name):
    if Movie.objects.filter(title=name).exists():
        movie = Movie.objects.get(title=name)
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)
    else:
        api_key = '1154146a'
        url = 'https://www.omdbapi.com/?t={}&apikey={}'.format(name, api_key)
        response = requests.get(url).json()

        movie = Movie.objects.create(
            title = response['Title'],
            year = response['Year'],
            rated = response['Rated'],
            released = response['Released'],
            runtime = response['Runtime'],
            genre = response['Genre'],
            director = response['Director'],
            writer = response['Writer'],
            actors = response['Actors'],
            plot = response['Plot'],
            language = response['Language'],
            country = response['Country'],
            awards = response['Awards'],
            poster = response['Poster'],
            imdbRating = response['imdbRating'],
            type = response['Type'],
            dvd = response['DVD'],
            box_office = response['BoxOffice'],
            production = response['Production']
        )

        data = {
            'Title' : response['Title'],
            'Year' : response['Year'],
            'Rated': response['Rated'],
            'Released': response['Released'],
            'Runtime': response['Runtime'],
            'Genre': response['Genre'],
            'Director': response['Director'],
            'Writer': response['Writer'],
            'Actors': response['Actors'],
            'Plot': response['Plot'],
            'Language': response['Language'],
            'Country': response['Country'],
            'Awards': response['Awards'],
            'Poster': response['Poster'],
            'imdbRating': response['imdbRating'],
            'Type': response['Type'],
            'DVD': response['DVD'],
            'BoxOffice' : response['BoxOffice'],
            'Production' : response['Production']
        }

        serializer = MovieSerializer(data = movie)
        if serializer.is_valid():
            serializer.save()

        return Response(data)


@api_view(['POST'])
def createComment(request):
    comment_data = request.data
    new_comment = Comment.objects.create(
        description = comment_data['description'],
        movie = Movie.objects.get(id=comment_data['movie_id'])
    )

    new_comment.save()
    serializer = CommentSerializer(new_comment)
    return Response(serializer.data)


@api_view(['GET'])
def allComments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewComment(request, pk):
    comments = Comment.objects.get(id = pk)
    serializer = CommentSerializer(comments, many=False)
    return Response(serializer.data)
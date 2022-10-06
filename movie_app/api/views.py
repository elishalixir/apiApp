from rest_framework.response import Response
from .serializers import MovieSerializer
from movie_app.models import Movie
from rest_framework.decorators import api_view


# Create your views here.
@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serialized = MovieSerializer(movies, many=True)  # Allows the full list of data to display once
    return Response(serialized.data)


@api_view()
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)  # Allows search using the pk in the url
    serialized = MovieSerializer(movie)
    return Response(serialized.data)

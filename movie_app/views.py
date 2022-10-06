# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .models import Movie
#
# # Create your views here.
#
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         "movies": list(movies.values())
#     }
#     print(movies)
#     print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#     print(data)
#     return JsonResponse(data)
#
# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)
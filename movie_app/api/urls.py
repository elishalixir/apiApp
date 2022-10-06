from django.urls import path
from . import views

urlpatterns = [
    path('mlist/', views.movie_list, name='mlist'),
    path('<int:pk>/', views.movie_detail, name='mdetail'),
]

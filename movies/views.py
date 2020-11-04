from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from .request import get_movies,get_movie,search_movie


def all_movies(request):
  popular_movies = get_movies('popular')
  upcoming_movies = get_movies('upcoming')
  now_showing_movies = get_movies('now_playing')
  
  return render(request,'movie-list/all-movies.html',{"popular_movies":popular_movies,"upcoming_movies":upcoming_movies,"now_showing_movies":now_showing_movies})

def movie(request,id):
  '''
  View movie page function that returns the movie details page and its data
  '''
  movie = get_movie(id)
  title =f'{movie.movie_title}'
  
  return render(request,'movie-list/movie.html',{"title":title,"movie":movie})

def search(request):
    '''
    View function to display the search results
    '''
    if 'movie':
      movie_name = request.GET.get("movie")
      movie_name_list = movie_name.split(" ")
      movie_name_format = "+".join(movie_name_list)
      searched_movies = search_movie(movie_name_format)
      title = f'search results for {movie_name}'
    return render(request,'movie-list/search.html',{"title":title,"movies":searched_movies})
  
    
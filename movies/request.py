import urllib.request,json
from .models import Movie

api_key =''
base_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

def get_movies(category):
  '''
  function to get json respomce
  '''
  get_movie_url = base_url.format(category,api_key)
  
  with urllib.request.urlopen(get_movie_url) as url:
    get_movie_data = url.read()
    get_movie_response = json.loads(get_movie_data)
    
    movie_results = None
    
    if get_movie_response['results']:
      movie_results_lists = get_movie_response['results']
      movie_results = process_results(movie_results_lists)
  
  return movie_results

def process_results(movie_list):
  '''
  function that processes the movie result and transform them to a list of Objects
  Args:
      movie_list: a list of dictionaries that contain movie details
  Returns:
      movie_results: a list of movie objects    
  '''
  movie_results = []
  for movie_item in movie_list:
    movie_id = movie_item.get('id')
    movie_title = movie_item.get('original_title')
    overview = movie_item.get('overview')
    poster = movie_item.get('poster_path')
    
    if poster:
      movie_object = Movie(movie_id,movie_title,overview,poster)
      movie_results.append(movie_object)
      
  return movie_results


def get_movie(id):
  get_movie_details_url = base_url.format(id,api_key)
  with urllib.request.urlopen(get_movie_details_url) as url:
    movie_details_data = url.read()
    movie_details_response = json.loads(movie_details_data)
    movie_object = None
    if movie_details_response:
      movie_id = movie_details_response.get('id')
      movie_title = movie_details_response.get('original_title')
      overview = movie_details_response.get('overview')
      poster = movie_details_response.get('poster_path')
      movie_object = movie_details_response = Movie(movie_id,movie_title,overview,poster)
          
  return movie_object

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results

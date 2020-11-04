from django.db import models

class Movie:
  
  def __init__(self,movie_id,movie_title,overview,poster):
    
    self.movie_id = movie_id
    self.movie_title = movie_title
    self.overview = overview
    self.poster = poster
  
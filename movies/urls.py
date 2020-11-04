from django.conf.urls import url
from . import views

urlpatterns=[
  url(r'^$',views.all_movies,name='allmovies'),
  url(r'^movie/(\d+)',views.movie,name='single_movie'),
  url(r'^search/',views.search,name='search'),
]
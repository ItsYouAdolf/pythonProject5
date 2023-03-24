from django.shortcuts import render
from .models import Movie2
from django.views.generic import ListView, DetailView
# Create your views here.

class MoviesView(ListView):
    model = Movie2
    queryset = Movie2.objects.filter(draft=False)
    paginate_by = 9
    template_name = 'novosti.html'


class MovieDetailView(DetailView):
    model = Movie2
    slug_field = 'url'
    template_name = 'novosti_detail.html'


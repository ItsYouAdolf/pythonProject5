from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie, Category, Actor, Genre
from .forms import ReviewForm
from django.db.models import Q

# Crate your views here.



class GenreYears():
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')




class MoviesView(GenreYears, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    paginate_by = 9
    template_name = 'kino.html'


class MovieDetailView(GenreYears, DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'kino_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = ReviewForm()
        return context

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect('kino')


class ActorView(GenreYears, DetailView):
    model = Actor
    template_name = 'actor.html'
    slug_field = 'name'


class FilterMoviesView(GenreYears, ListView):
    template_name = "kino.html"
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) | Q(genres__in=self.request.GET.getlist('genre'))
        )
        return queryset


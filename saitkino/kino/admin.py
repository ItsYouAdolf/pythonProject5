from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'



class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')

class MovieShotsInline(admin.StackedInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="75px" height="100px">')

    get_image.short_description = 'Изображение'


@admin.register(Movie, site=None)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft', 'get_image',)
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    form = MovieAdminForm
    fields = (('title', 'tagline', 'year', 'country'), 'description', 'poster', ('directors', 'actors', 'genres'),
              'world_premiere', ('fees_in_usa', 'fees_in_world'), 'category', 'url', 'draft', 'get_image',)

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="75px" height="100px">')

    get_image.short_description = 'Изображение'

@admin.register(Reviews, site=None)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'movie', 'id')
    readonly_fields = ('name', 'email')



@admin.register(Actor, site=None)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="75px" height="100px">')

    get_image.short_description = 'Изображение'


@admin.register(MovieShots, site=None)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image',)
    search_fields = ('title', 'movie')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="75px" height="100px">')

    get_image.short_description = 'Изображение'

@admin.register(Category, site=None)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)







admin.site.register(Genre)
admin.site.register(RatingStar)
admin.site.register(Rating)

admin.site.site_title = 'Django-Kino'
admin.site.site_header = 'Django-Kino'

"""Cinematic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MoviesPopular),
    path('movies/playing', views.MoviesPlaying),
    path('movies/upcoming', views.MoviesUpcoming),
    path('movies/top', views.MoviesTopRated),
    
    path('tv/popular', views.ShowsPopular),
    path('tv/onair', views.ShowsOnAir),
    path('tv/airing', views.ShowsAiring),
    path('tv/top', views.ShowsTopRated),
    
    path('people', views.People),
    path('<str:type>/id=<str:id>', views.Details),
    path('<str:type>/keyword=<str:key>', views.Search),
    path('detail/people/id=<str:id>', views.PeopleDetails),

    path('speech', views.SpeechRecognition)
]
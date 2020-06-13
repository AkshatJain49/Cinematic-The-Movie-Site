from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import pyttsx3
import speech_recognition as sr

def MoviesPopular(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        moviesList = result['results'] 
        binddata = {"moviesList" : moviesList, "type" : "popular"}
        return render(request, 'Movies.html', binddata)
    
    except:
        return render(request, 'Error.html', None)



def MoviesPlaying(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        moviesList = result['results'] 
        binddata = {"moviesList" : moviesList, "type" : "playing"}
        return render(request, 'Movies.html', binddata)
    
    except:
        return render(request, 'Error.html', None)



def MoviesUpcoming(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        moviesList = result['results'] 
        binddata = {"moviesList" : moviesList, "type" : "upcoming"}
        return render(request, 'Movies.html', binddata)

    except:
        return render(request, 'Error.html', None)



def MoviesTopRated(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        moviesList = result['results'] 
        binddata = {"moviesList" : moviesList, "type" : "topRated"}
        return render(request, 'Movies.html', binddata)
    
    except:
        return render(request, 'Error.html', None)



def ShowsPopular(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/tv/popular?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        showsList = result['results']
        binddata = {"showsList" : showsList, "type" : "popular"}
        return render(request, 'Shows.html', binddata)
    
    except:
        return render(request, 'Error.html', None)
        


def ShowsOnAir(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/tv/on_the_air?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        showsList = result['results']
        binddata = {"showsList" : showsList, "type" : "playing"}
        return render(request, 'Shows.html', binddata)
    
    except:
        return render(request, 'Error.html', None)



def ShowsAiring(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/tv/airing_today?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        showsList = result['results']
        binddata = {"showsList" : showsList, "type" : "upcoming"}
        return render(request, 'Shows.html', binddata)

    except:
        return render(request, 'Error.html', None)



def ShowsTopRated(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/tv/top_rated?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        showsList = result['results']
        binddata = {"showsList" : showsList, "type" : "topRated"}
        return render(request, 'Shows.html', binddata)
    
    except:
        return render(request, 'Error.html', None)



def People(request):
    try:
        response = requests.get("https://api.themoviedb.org/3/person/popular?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1")
        result = response.json()
        peopleList = result['results']
        binddata = {"peopleList" : peopleList}
        return render(request, 'People.html', binddata)

    except:
       return render(request, 'Error.html', None)



def Details(request, type, id):
    try:
        if type == "movie":
            urlDetails = "https://api.themoviedb.org/3/movie/" + id + "?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US"
            urlTrailers = "https://api.themoviedb.org/3/movie/"+ id +"/videos?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US"
            urlCast  = "https://api.themoviedb.org/3/movie/" + id + "/credits?api_key=83b2f8791807db4f499f4633fca4af79"
            urlSimilar = "https://api.themoviedb.org/3/movie/"+ id +"/similar?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1"
            urlReviews = "https://api.themoviedb.org/3/movie/"+ id +"/reviews?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1"

        else:
            urlDetails = "https://api.themoviedb.org/3/tv/"+ id +"?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US"
            urlTrailers = "https://api.themoviedb.org/3/tv/"+ id +"/videos?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US"
            urlCast = "https://api.themoviedb.org/3/tv/" + id + "/credits?api_key=83b2f8791807db4f499f4633fca4af79"
            urlSimilar = "https://api.themoviedb.org/3/tv/"+ id +"/similar?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1"
            urlReviews = "https://api.themoviedb.org/3/tv/"+ id +"/reviews?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1"

        responseDetail = requests.get(urlDetails)
        resultDetail = responseDetail.json()

        responseTrailer = requests.get(urlTrailers)
        resultTrailer = responseTrailer.json()
        trailerList = resultTrailer['results']
        
        responseCast = requests.get(urlCast)
        resultCast = responseCast.json()
        castList = resultCast['cast']
        
        responseSimilar = requests.get(urlSimilar)
        resultSimilar = responseSimilar.json()
        similarList = resultSimilar['results']

        responseReviews = requests.get(urlReviews)
        resultReviews = responseReviews.json()
        reviewList = resultReviews['results']

        binddata = {"information" : resultDetail, "trailerList" : trailerList, "castList" : castList, "similarList" : similarList, "reviewList" : reviewList, "type": type}
        return render(request, 'Details.html', binddata)

    except:
        return render(request, 'Error.html', None)



def Search(request, type, key):
    try:
        if type == "movie":
            response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&query=" + key +"&page=1")
        
        else:
            response = requests.get("https://api.themoviedb.org/3/search/tv?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US&page=1&query=" + key)

        result = response.json()
        searchList = result['results']
        binddata = {"searchList" : searchList, "type" : type}
        return render(request, 'Search.html', binddata)
    
    except:
        return render(request, 'Error.html', None)



def PeopleDetails(request, id):
    responseDetails = requests.get("https://api.themoviedb.org/3/person/"+ id +"?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US")
    responseMovies = requests.get("https://api.themoviedb.org/3/person/"+ id +"/movie_credits?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US")
    responseShows = requests.get("https://api.themoviedb.org/3/person/"+ id +"/tv_credits?api_key=83b2f8791807db4f499f4633fca4af79&language=en-US")
    
    resultDetails = responseDetails.json()
    resultMovies = responseMovies.json()
    resultShows = responseShows.json()

    moviesList = resultMovies['cast']
    showsList = resultShows['cast']

    binddata = {"information" : resultDetails, "moviesList" : moviesList, "showsList" : showsList}
    return render(request, 'PeopleDetails.html', binddata)



def SpeechRecognition(request):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    try:
        print("Recognising")
        query = r.recognize_google(audio)
        engine.say("You Searched For " + query)
        engine.runAndWait()
        print("USER SAID: ", query)
        

    except:
        engine.say("Unable to Recognize")
        engine.runAndWait()
        print("Say that Again")
        query = "None"

    return HttpResponse(query)
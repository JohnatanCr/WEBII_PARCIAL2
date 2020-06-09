from django.shortcuts import render , HttpResponse
from .models import Movie
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json
#from .models import ValidateFormSerializer
from firstapp.JsonCheck import revisarJson
def movies(request):
    if request.method == 'GET':
        response_data = {}
        response_data["movies"] = []
        for i in Movie.objects.all():
            obj = {}
            obj["movietitle"] = i.movietitle
            obj['movieid'] = i.movieid
            response_data["movies"].append(obj)

        response_data['result'] = 'success'
        return JsonResponse(response_data, status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Request'
        return JsonResponse(response_data, status=403)

def postGetLogin(request):
    return HttpResponse("GETUSERLOGIN")

def postClientList(request):
    return HttpResponse("GETCLIENTLIST")

def updateclient(request):
    return HttpResponse("UPDATE CLIENT")

def getclient(request):
    return HttpResponse("GET CLIENT")

def deleteclient(request):
    return HttpResponse("DETELE CLIENT")

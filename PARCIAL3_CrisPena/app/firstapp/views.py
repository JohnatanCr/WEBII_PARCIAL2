from django.shortcuts import render , HttpResponse
from .models import Estados
from .models import Movie
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import json
from firstapp.JsonCheck import revisarJson

def vista(request):
    return render(request, 'index.html')

def state(request, id):
    if request.method == 'GET':
        response_data = {}
        try:
            obj = Estados.objects.get(id=id)
            response_data['result'] = 'success'
            response_data['name'] = obj.name
            response_data['clave'] = obj.clave
            response_data['abrev'] = obj.abrev
            response_data['riskIndex'] = obj.risk
            return JsonResponse(response_data, status=200)
        except Estados.DoesNotExist:
            response_data['result'] = 'error'
            response_data['message'] = 'ID NOT FOUND'
            return JsonResponse(response_data, status=400)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Request'
        return JsonResponse(response_data, status=403)

def states(request):

    if request.method == 'GET':
        response_data = {}
        response_data["estados"] = []
        for i in Estados.objects.all():
            obj = {}
            obj["name"] = i.name
            obj['clave'] = i.clave
            obj['abrev'] = i.abrev
            obj['riskIndex'] = i.risk
            response_data["estados"].append(obj)

        response_data['result'] = 'success'
        return JsonResponse(response_data, status=200)
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Request'
        return JsonResponse(response_data, status=403)

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


def paito(request):
    if request.method == 'POST':

       #json_data = json.loads(request.body)
       #attr_error = False
       #if 'var1' not in json_data:
       #    attr_error = True
       #elif 'var2' not in json_data:
       #    attr_error = True
       #elif 'var3' not in json_data:
       #    attr_error = True

       #if attr_error == True:
       #    response_data = {}
       #    response_data['result'] = 'Error'
       #    response_data['message'] = 'invalid Json'
       #    return JsonResponse(response_data, status=200)
       #else:
       #    response_data = {}
       #    response_data['result'] = 'success'
       #    response_data['message'] = 'valid Json'
       #    return JsonResponse(response_data, status=400)

        #VIA FUNCTION
        response_data = {}
        isJson = isJson(request.body)
        if isJson == True:
            response_data['result'] = 'success'
            response_
            data['message'] = 'valid Json'
            return JsonResponse(response_data, status=200)
        else:
            response_data['result'] = 'error'
            response_data['message'] = 'invalid Json'
            return JsonResponse(response_data, status=200)

        #DIRECT
        #response_data = {}

        #try:
        #    json_object = json.loads(request.body)
        #except ValueError as e:
        #    response_data['result'] = 'error'
        #    response_data['message'] = 'Invalid Json'
        #    return JsonResponse(response_data, status=401)
        #
        #response_data['result'] = 'success'
        #response_data['message'] = 'valid Json'
        #return JsonResponse(response_data, status=200)


        #valid_ser = ValidateFormSerializer(data=request.body)
        #if valid_ser.is_valid():
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Invalid Request'
        return JsonResponse(response_data, status=403)
        #return HttpResponse("ADIOS")

def paito2(request):
    json_data = json.loads(request.body)
    if request.method == 'GET':
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = 'Invalid Request'
        return JsonResponse(response_data)
        #return HttpResponse("HOLA %s" % json_data["HOLA"], content_type='application/json')
    else:
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = 'Método inválido'
        return JsonResponse(response_data, status=401)
        #return HttpResponse(response_data, content_type='application/json');

    #print(json_data)
    #for product in products['products']:
     # print product['part_number']
      #print product['product_name']
      #print product['quantity']




def updateclient(request):
    return HttpResponse("UPDATE CLIENT")

def getclient(request):
    return HttpResponse("GET CLIENT")

def deleteclient(request):
    return HttpResponse("DETELE CLIENT")

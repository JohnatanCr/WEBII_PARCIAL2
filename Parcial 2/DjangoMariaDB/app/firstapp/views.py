# Create your views here.
#IMPORT models
from .models import Movie,ApiUsers

#IMPORT LIBRARIRES/FUNCTIONS
#from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
from firstapp.customClasses import *
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash
def isJson(myJson):
    try:
        json_object = json.loads(myJson)
    except ValueError as e:
        return False
    return True
def login(request):

    #VALIDATE METHOD
    responseData = {}
    if request.method == 'POST':
        #DECLARE RESPONS
        responseMessage = ""
        #CHECK JSON STRUCTURE
        is_Json = isJson(request.body)
        if (is_Json):
            jsonData = json.loads(request.body)
            #CHECK JSON CONTENT
            if "user" not in jsonData:
                responseMessage = "missing USER, requiered"
            elif "password" not in jsonData:
                responseMessage = "missing PASSWORD, requiered"
            #CHECK IF USER EXIST
            else:
                try:
                    print("PASE AQUI")
                    userDB = ApiUsers.objects.get(user = jsonData['user'])
                except Exception as e:
                    responseMessage = "The user does not exist"
                    responseData['result'] = 'error'
                    responseData['message'] = responseMessage
                    return JsonResponse(responseData,status=401)
                #TAKE PASSWORD OF THE USER
                password = jsonData['password']
                currentPasswordHash = userDB.password
                #CHECK IF PASSWORD IS CORRECT
                if (check_password(password,currentPasswordHash) == False):
                    responseMessage = "The user does not exist or the password is incorrect"
                #CHECK IF USER HAS API-KEY
                elif (userDB.api_key == None):
                    genApiKey = ApiKey().generate_key_complex()
                    userDB.api_key = genApiKey
                    userDB.save()

            if (responseMessage != ""):
                responseData['result'] = 'ERROR'
                responseData['message'] = responseMessage
                return JsonResponse(responseData, status=401)
            else:
                responseData['result'] = 'SUCCSESS'
                responseData['message'] = 'Valid Credentials'
                responseData['userApiKey'] = userDB.api_key
                return JsonResponse(responseData,status=200)
        else:
            responseData['result'] = 'ERROR'
            responseMessage = "JSON Invalid Structure"
            responseData['message'] = responseMessage

        #RETURN RESPONSE
        #print(responseMessage)
        return JsonResponse(responseData)
    else:
        responseData['result'] = 'error'
        responseData['message'] = 'no es post'
        return JsonResponse(responseData, status=400)


def makepassword(request,password):
    hashPassword = make_password(password)
    response_data = {}
    response_data['password'] = hashPassword
    return JsonResponse(response_data, status=200)

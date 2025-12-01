import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

#Response
def TypesOfReponse(request):
    return HttpResponse('Plane Text Response')
    return HttpResponse(10)
    return HttpResponse(False)
    return HttpResponse(JsonResponse({'Name': 'Raihan', 'age': "18"}))
    return HttpResponseRedirect('/')
    return HttpResponseNotFound('Page Not Found')
    return HttpResponse('Status Code', status=202)


    #Custom Header
    responses = HttpResponse("Plane Text")
    responses['token'] = '784001'
    return responses


    #Responses Cookies
    responses = HttpResponse("Plane Text Response with Cookie")
    responses.set_cookie("Text_Cookie", value="784001adf")
    return responses


#Request
@csrf_exempt
def TypesOfRequest(request):
    if request.method == 'POST':
        return HttpResponse('POST Method')

    if request.method == 'GET':
        return HttpResponse('GET Method')

    if request.method == 'PUT':
        return HttpResponse('PUT Method')

    if request.method == 'PATCH':
        return HttpResponse('PATCH Method')

    if request.method == 'DELETE':
        return HttpResponse('DELETE Method')


#Query String
def QueryString(request):
    name = request.GET.get('name')
    city = request.GET.get('city')
    return HttpResponse(f"Query String: {name}, {city}")


#Query String Custom Header
def CustomHeader(request):
    mytoken = request.headers.get('mytoken')
    password = request.headers.get('password')
    return HttpResponse(f"Query String: {mytoken}, {password}")


@csrf_exempt
def FormData(request):
    if request.method == 'POST':
        data = request.POST.dict()
        return JsonResponse(data)

@csrf_exempt
def RequestBody(request):
    if request.method == 'POST':
        data = json.loads(request.body)
    return JsonResponse(data)

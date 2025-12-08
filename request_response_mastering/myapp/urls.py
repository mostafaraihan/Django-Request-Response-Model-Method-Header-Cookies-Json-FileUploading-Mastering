from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index),
    path("TypesOfReponse/", views.TypesOfReponse),
    path("TypesOfRequest/", views.TypesOfRequest),
    path("QueryString/", views.QueryString),
    path("CustomHeader/", views.CustomHeader),
    path("FormData/", views.FormData),
    path("RequestBody/", views.RequestBody),
    path("FileDownload/", views.FileDownload),
]

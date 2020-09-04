from django.shortcuts import render
import  requests
import  json

from app1.models import PrincingTables,PrincingTablesSerializer

from rest_framework.viewsets import ModelViewSet

class  PrincingTablesViewsets(ModelViewSet):
    queryset = PrincingTables.objects.all()
    serializer_class = PrincingTablesSerializer


def display(request):
       c1=requests.get("http://127.0.0.1:8000/showapi/")
       result=c1.json()
       print(result)
       return  render(request,"index.html",{"PrincingTables":result})


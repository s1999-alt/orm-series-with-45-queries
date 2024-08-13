from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum, Q, Min, Max



def index(request):
  author = Books.objects.all().filter(author__pk=1).aggregate(Sum('price'))
  print(author)
  res = ''
  for i in author:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)

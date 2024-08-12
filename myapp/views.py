from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum



def index(request):
  author = Books.objects.all().filter(author__firstname__contains='a').values_list('title', flat=True)
  print(author)
  res = ''
  for i in author:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)

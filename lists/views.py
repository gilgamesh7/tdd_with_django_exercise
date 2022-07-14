from django.shortcuts import render
from django.http import HttpResponse

home_page=None
def home_page(request):
    return HttpResponse("return this string")


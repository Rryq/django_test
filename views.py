from django.http import HttpResponse

def index(request):
    return HttpResponse('hello python')

def index2(request):
    return HttpResponse('hello world')


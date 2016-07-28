from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
      return render(request, 'blog/post_list1.html',{})

def post_list_2(request):
      return render(request, 'blog/post_list.html', {})

# Create your views here.
def mysum(request, x, y=0, z=0):
      return HttpResponse(int(x) + int(y) + int(z))

def mysum2(request, x):
      result = sum(int(i) for i in x.split('/'))
      return HttpResponse(result)

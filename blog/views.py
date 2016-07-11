from django.shortcuts import render

def post_list(request):
      return render(request, 'blog/post_list1.html',{})

def post_list_2(request):
      return render(request, 'blog/post_list.html', {})

# Create your views here.


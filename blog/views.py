from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.forms import CommentModelForm
from blog.models import Post, Comment


def post_list(request):
      return render(request, 'blog/post_list1.html',{})

def post_list_2(request):
      return render(request, 'blog/post_list.html', {})

def post_detail(request):
      return render(request, 'Blog/post_detail.html', {})


# Create your views here.
def mysum(request, x, y=0, z=0):
      return HttpResponse(int(x) + int(y) + int(z))

def mysum2(request, x):
      result = sum(int(i) for i in x.split('/'))
      return HttpResponse(result)


def comment_new(request):
    if request.method=='POST':
        form=CommentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form =CommentModelForm()
    return render(request, 'blog/form_html.html', {'form':form})

def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        fvorm = CommentModelForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CommentModelForm(instance=comment)
        return render(request, 'blog/comment_form.html', {
         'form': form,
     })



def p_list(request):
      qs=Post.objects.all()
      return render(request, 'blog/post_list.html', {
            'post_list':qs,
            })


def postd_list(request):
      qs=Post.objects.all()
      return render(request, 'blog/post_detail.html', {
            'post_list':qs,
})


def comment_list(request):
      qs=Comment.objects.all()
      return render(request, 'blog/comment_list.html', {
            'comment_list':qs,
            })







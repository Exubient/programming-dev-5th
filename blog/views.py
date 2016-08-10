from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import CommentModelForm, PostModelForm, CommentForm, CommentForm1
from blog.models import Post, Comment, Comment1
from django.http import Http404


def post_list(request):
      return render(request, 'blog/post_list1.html',{'post_list': Post.objects.all()})

def post_list_2(request):
      return render(request, 'blog/post_list.html', {})

def post_detail(request, pk):
      try:
          post= Post.objects.get(pk=pk)
      except Post.DoesNotExist:
          raise Http404
      return render(request, 'blog/post_html1.html', { 'post':post,})

# ==as post = get_object_or_404(Post, pk=pk)


# Create your views here.
def mysum(request, x, y=0, z=0):
      return HttpResponse(int(x) + int(y) + int(z))

def mysum2(request, x):
      result = sum(int(i) for i in x.split('/'))
      return HttpResponse(result)


def post_new(request):
    if request.method=='POST':
        form=PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form =PostModelForm()
    return render(request, 'blog/post_html.html', {'form':form})


def comment_new(request):

    if request.method=='POST':
        form=CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form =CommentModelForm()
    return render(request, 'blog/form_html.html', {'form':form})

def comment_new1(request):
    if request.method=='POST':
        form=CommentForm1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentForm1()
    return render(request, 'blog/test.html', {'form':form})

def comment_edit(request, post_pk, pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm2(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, '댓글을 수정했습니다.')
            return redirect(post)
    else:
        form = CommentForm2(instance=comment)

    return render(request, 'blog/comment_form.html', {
        'form': form,
    })





def comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            comment.save()
            comments = Comment1.objects.order_by('pk').reverse()
            return render(request, 'blog/test.html', {'comments': comments})
    else:
        form = CommentForm()
    comments = Comment1.objects.order_by('pk').reverse()
    return render(request, 'blog/test.html',
        {'comments': comments})



def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES, instance=comment)
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







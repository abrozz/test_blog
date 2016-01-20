from django.http import HttpResponseRedirect
from .models import Post
from .forms import post_forms
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def index(request):

    post_list = Post.objects.order_by('-id')[:20]
    context = {'post_list': post_list}


    return render(request, 'blog/index.html', context)



def add(request):
    if request.method == 'POST':
        form = post_forms(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.title = (request.POST ['title'])
            p.dtc = timezone.now()
            p.save()
            return HttpResponseRedirect('/blog/')
    else:

        formset = post_forms()
        return render(request, 'blog/add.html', {'formset': formset})

def edit(request, id):
     a = Post.objects.get(pk=id)
     if request.method == 'POST':
         form = post_forms(request.POST, instance=a)
         if form.is_valid():
            p = form.save(commit=False)
            p.title = (request.POST ['title'])
            p.dtm=timezone.now()
            p.save()
            return HttpResponseRedirect('/blog/')
     else:
         formset = post_forms(instance=a)
         return render(request, 'blog/edit.html', {'formset': formset})

def delete_post(request, id):
    a = Post.objects.get(pk=id)
    if request.method == 'POST':
        p = Post.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect('/blog/')
    else:
        return render(request, 'blog/delete_post.html')
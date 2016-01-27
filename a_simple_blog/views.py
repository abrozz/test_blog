from django.http import HttpResponseRedirect
from .models import Post
from .forms import post_forms
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PublisherList(ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = Post.objects.order_by('-id')[:20]
    context_object_name = 'post_list'

class PostCreate(CreateView):
    form_class = post_forms
    model = Post
    template_name = 'blog/add.html'
    context_object_name = 'formset'
    def form_valid(self, form):
        p = form.save(commit=False)
        p.dtc = timezone.now()
        p.save()
        return HttpResponseRedirect('/blog/')

class PostUpdate(UpdateView):
    form_class = post_forms
    model = Post
    template_name = 'blog/edit.html'
    def form_valid(self, form):
        p = form.save(commit=False)
        p.dtm = timezone.now()
        p.save()
        return HttpResponseRedirect('/blog/')

class PostDelete(DeleteView):
    form_class = post_forms
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = ('/blog/')

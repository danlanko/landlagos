from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from .models import NewPost
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect
from .forms import NewPostForm
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


class NewPostView(generic.CreateView):
    model = NewPost
    template_name = 'backend/blog/new_post.html'
    form_class = NewPostForm
    success_url = reverse_lazy('new_post')

    def form_valid(self, form):
        with transaction.atomic():
            messages.success(self.request, 'Success, new post was created.')
        return super(NewPostView, self).form_valid(form)


class PostList(generic.ListView):
    model = NewPost
    template_name = 'backend/blog/all_post.html'


class PostEdit(generic.UpdateView):
    model = NewPost
    template_name = 'backend/blog/new_post.html'
    form_class = NewPostForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        with transaction.atomic():
            today = datetime.today()
            form.instance.last_edited = today
            form.save()
            messages.success(self.request, 'You post was edited successfully')
        return super(PostEdit, self).form_valid(form)


# @login_required()
def delete_post(request, blog_id):
    get_blog = NewPost.objects.get(id=blog_id)
    get_blog.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('post_list')


# @login_required()
def approve_post(request, blog_id):
    get_blog = NewPost.objects.get(id=blog_id)
    get_blog.publish = True
    get_blog.save()
    messages.success(request, 'Blog Post Approved successfully')
    return redirect('post_list')


# @login_required()
def disapprove_post(request, blog_id):
    get_blog = NewPost.objects.get(id=blog_id)
    get_blog.publish = False
    get_blog.save()
    messages.success(request, 'Blog Post Dis-Approved successfully')
    return redirect('post_list')

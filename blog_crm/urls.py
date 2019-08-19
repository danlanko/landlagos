from django.urls import path
from .views import *


urlpatterns = [

    path('', NewPostView.as_view(), name='new_post'),
    path('all_blog_post/', PostList.as_view(), name='post_list'),
    path('edit_blog_posy/<slug>/', PostEdit.as_view(), name='edit_blog_post'),
    path('blog_post_delete/<blog_id>/', delete_post, name='delete_post'),
    path('blog_approve_post/<blog_id>/', approve_post, name='approve_post'),
    path('blog_dis_approve_post/<blog_id>/', disapprove_post, name='disapprove_post'),

]
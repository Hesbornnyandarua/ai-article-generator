from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login', views.user_login, name='user_login'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('generate-blog', views.generate_blog, name='generate_blog')
    path('blog-list', views.blog_list, name='blog-list')
    path('blog-details/<int:pk>/', views.blog_details, name='blog-details')

]
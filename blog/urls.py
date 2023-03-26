from django import http, views
from django.urls import path
from . import views

#http://127.0.0.1:8000/         => homepage
#http://127.0.0.1:8000/index    => homepage
#http://127.0.0.1:8000/about    => aboutpage
#http://127.0.0.1:8000/contact  => contact
#http://127.0.0.1:8000/signup  => sign up page
#http://127.0.0.1:8000/blogs    => blogs
#http://127.0.0.1:8000/blogs/3  => blog-details

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("about", views.about),
    path("contact", views.contact),
    path("signup", views.signup),
    path("blogs", views.index),
    path("blogs/<int:id>", views.blog_details),
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
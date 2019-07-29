from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('blog/'+'<int:blog_id>', views.detail1, name="detail1"),
    path('dealerboard/'+'<int:blog_id>', views.detail2, name="detail2"),
    path('questionboard/'+'<int:blog_id>', views.detail3, name="detail3"),
    path('freeboardNew/', views.freeboardNew, name="freeboardNew"),
    path('dealerboardNew/', views.dealerboardNew, name="dealerboardNew"),
    path('questionNew/', views.questionNew, name="questionNew"),
    path('blog/blogCreate', views.blogCreate, name="blogCreate"),
    path('dealerboard/dealerCreate', views.dealerCreate, name="dealerCreate"),
    path('questionboard/questionCreate', views.questionCreate, name="questionCreate"),
    path('freeboard/', views.freeboard, name="freeboard"),
    path('dealerboard/', views.dealerboard, name="dealerboard"),
    path('questionboard/', views.questionboard, name="questionboard"),
]
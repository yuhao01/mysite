from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    ]
from django.urls import path
from rioz import views 

app_name = 'rioz'

urlpatterns = [
    path('', views.home, name='home'),
    path("user_logout/", views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='login'),
    path('contact/', views.messageForm, name='message_form'),
    path('messages/', views.message_user, name='messages'),
    path('messages/delete/<pk>/', views.messages_delete, name='delete_messages'),
    path('resume/', views.resume_view, name='resume'),
    path('experience/', views.experience_view, name='experience'),
    path('clients/', views.client_manage, name='client_manage'),
    path('clients/delete/<pk>/', views.client_delete, name='client_delete'),
    path('blogs/', views.blog, name='blog'),
    path('blogs/<pk>/', views.blog_detail, name='blog_detail'),
    path('comments/<pk>/', views.delete_comment, name='delete_comment'),
]
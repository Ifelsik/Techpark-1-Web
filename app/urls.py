from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hot', views.hot, name='hot'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
    path('questions/<int:question_id>', views.question, name='question'),
    path('ask', views.ask, name='ask'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('settings', views.settings, name='settings')
]
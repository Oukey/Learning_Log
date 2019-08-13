from django.shortcuts import render
from . models import Topic

def index(request):
    '''Домашняя страница приложения Learning_log'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''Выводит список тем'''
    topics = Topic.objects.order_by('date_added')  # запрос к БД на получение объекта Topic
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

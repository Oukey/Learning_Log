from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm


def index(request):
    '''Домашняя страница приложения Learning_log'''
    return render(request, 'learning_logs/index.html')


def topics(request):
    '''Выводит список тем'''
    topics = Topic.objects.order_by('date_added')  # запрос к БД на получение объекта Topic
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    '''Выводит одну тему и все её записи'''
    topic = Topic.objects.get(id=topic_id)  # Запрос к БД
    entries = topic.entry_set.order_by('-date_added')  # Запрос к БД, '-date_added' сортирует id в обратом порядке
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    '''Определяет новую тему'''
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные
        form = TopicForm(request.POST)
        if form.is_valid():  # Прверка отправленной информации
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()  # Запись информации из формы в базу данных
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # возврат на страницу topics
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

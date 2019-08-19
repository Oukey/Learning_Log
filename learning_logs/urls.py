# urls.py
'''Определяет схемы URL для learning_logs'''

from django.urls import path, include, re_path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),  # (регулярное выражение, url, index)
    # Вывод всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией, по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # СТраница для добавления новой записи
    path('new_entry/<int:topic_id/', views.new_entry, name='new_entry'),

]

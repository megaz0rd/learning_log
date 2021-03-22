"""Learning_logs url patterns"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # topics page
    path('topics/', views.topics, name='topics'),
    # topic page detail
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page for new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page for edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/polls/', views.index, name='index'),
    path('/polls/5/<int:question_id>/', views.detail, name='detail'),
    path('/polls/5/results/', views.results, name='results'),
    path('/polls/5/vote/', views.vote, name='vote'),
]

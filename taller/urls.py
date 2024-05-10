from django.urls import path

from . import views

app_name = "taller"
urlpatterns = [
    # # ex: /polls/
    # path("", views.index, name="index"),
    # # ex: /polls/5/
    # path("polls/<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("polls/<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("polls/<int:question_id>/vote/", views.vote, name="vote"),
    
    path("", views.IndexView.as_view(), name="index"),
    path("polls/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("polls/<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("polls/<int:question_id>/vote/", views.vote, name="vote"),
    
    path("taller/registro", views.RegistroIndexView.as_view(), name="registro"),
]

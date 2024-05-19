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
    
    
    # path("polls/<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("polls/<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("polls/<int:question_id>/vote/", views.vote, name="vote"),
    
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.index, name="index"),
    path("taller/registro", views.RegistroIndexView.as_view(), name="registro"),
    
    # path('taller/prioridades/', views.prioridad_list_view, name='prioridades-list'),
    path('taller/prioridades/', views.PrioridadListView.as_view(), name='prioridades-list'),
    path('taller/crear-prioridad/', views.create_prioridad_view, name='create-prioridad'),
    
    path('taller/equipos/', views.EquipoListView.as_view(), name='equipos-list'),
    path('taller/crear-equipo/', views.create_equipo_view, name='create-equipo'),
    
    path('taller/crear-registro/', views.create_registro_view, name='create-registro'),
    
    # asistentes para reportes
    path('taller/reporte-x-fecha/<str:reporte>/', views.date_selector, name='reporte-x-fecha'),
    path('taller/reporte-x-entidad/<str:reporte>/', views.entidad_selector, name='reporte-x-entidad'),
    path('taller/reporte-x-prioridad/<str:reporte>/', views.prioridad_selector, name='reporte-x-prioridad'),
    path('taller/reporte-x-especialista/<str:reporte>/', views.especialista_selector, name='reporte-x-especialista'),
    path('taller/reporte-x-estado/<str:reporte>/', views.estado_selector, name='reporte-x-estado'),
    
    # Gráficas:
    path('taller/graficas/detalle-x-entidad/', views.grafica_detalle_x_entidad, name='graficas-detalle-x-entidad'),
    path('taller/graficas/total-x-entidad/', views.grafica_total_x_entidad, name='graficas-total-x-entidad'),
]

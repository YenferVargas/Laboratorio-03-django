from django.urls import path


from . import views

app_name = 'encuesta'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pregunta_id>/', views.detalle, name='detalle'), # ex: /encuesta/5/resultados/
    path('<int:pregunta_id>/resultados/', views.resultados, name='resultados'), # ex: /encuesta/5/voto/
   path('<int:pregunta_id>/votar/', views.votar, name='votar'),
  
    
]
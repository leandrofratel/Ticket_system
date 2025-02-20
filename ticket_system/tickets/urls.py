from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('novo/', views.ticket_create, name='ticket_create'),
    path('editar/<int:pk>/', views.ticket_update, name='ticket_update'),
    path('excluir/<int:pk>/', views.ticket_delete, name='ticket_delete'),
    path('detalhes/<int:pk>/', views.ticket_detail, name='ticket_detail'),
]
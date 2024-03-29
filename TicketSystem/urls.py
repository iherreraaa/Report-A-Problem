from django.urls import path
from . import views

urlpatterns = [
    path('', views.triage, name='triage'),
    path('pending/', views.pending, name='pending'),
    path('unsolved/', views.unsolved, name='unsolved'),
    path('solved/', views.solved, name='solved'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('open/', views.open_ticket, name='open_ticket'),
    path('viewTicket/<int:ticket_id>/', views.view_ticket, name='view_ticket'),
]
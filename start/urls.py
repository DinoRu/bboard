from django.urls import path
from . import views

app_name = 'start'

urlpatterns = [
    path('', views.listing, name='listing'),
    path('<int:album_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('affichage/', views.affichage),
]
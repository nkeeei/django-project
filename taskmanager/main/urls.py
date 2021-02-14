from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('delete/<int:t_id>', views.delete, name='delete'),
    path('update/<int:t_id>', views.update, name='update'),
]

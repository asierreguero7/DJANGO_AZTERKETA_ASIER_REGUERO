from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('index/add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('index/add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('index/delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('index/update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('index/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexkotxeak, name='indexkotxeak'),
    path('index/', views.indexkotxeak, name='indexkotxeak'),
    path('add/', views.add, name='add'),
    path('index/add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('index/add/addrecord/', views.addrecord, name='addrecord'),
    path('deletekotxeak/<int:id>', views.deletekotxeak, name='deletekotxeak'),
    path('index/deletekotxeak/<int:id>', views.deletekotxeak, name='deletekotxeak'),
    path('update/<int:id>', views.update, name='update'),
    path('index/update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('index/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
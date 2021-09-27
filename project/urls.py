from django.contrib import admin
from django.urls import path
from app import views
from app import viewsProduto
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('create/', views.create, name='create'),
    path('view/<int:pk>/', views.view, name='view'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('produto/form/<int:pk>/', viewsProduto.form, name='form'),
    path('produto/<int:pk>/', views.produtos, name='produto'),
    path('produto/create/<int:pk>/', viewsProduto.create, name='create'),
    path('produto/home/<int:pk>/', viewsProduto.home, name='homeproduto'),
    path('produto/view/<int:pk>/', viewsProduto.view, name='view'),
    path('produto/edit/<int:pk>/', viewsProduto.edit, name='edit'),
    path('produto/update/<int:pk>/', viewsProduto.update, name='update'),
    path('produto/delete/<int:pk>/', viewsProduto.delete, name='delete'),
]
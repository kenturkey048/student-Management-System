from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:pk>', views.view_student, name='view_student'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('new/', views.new, name='new')
]

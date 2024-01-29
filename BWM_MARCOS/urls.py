from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name ='home'),
     # path('about/', views.about, name ='about'),
     
     path('detail/', views.detail, name ='detail'),
     path('detail_BWMMARCOS/', views.detail_BWMMARCOS, name ='detail_BWMMARCOS'),
     path('detail_ILP/', views.detail_ILP, name ='detail_ILP'),

     #Menu Kriteria
     path('kriteria/', views.view_kriteria, name='view_kriteria'),
     path('kriteria/create', views.create_kriteria, name = 'create-kriteria'),
     path('edit-kriteria/<int:pk>/', views.edit_kriteria, name='edit-kriteria'),
     path('delete-kriteria/<int:pk>/', views.delete_kriteria, name='delete-kriteria'),
     
     #Menu Nilai Kriteria
     # path('nilai-kriteria/', views.view_nilai_kriteria, name='view_nilai-kriteria'),
     # path('nilai-kriteria/create', views.create_nilai_kriteria, name = 'create-nilai-kriteria'),
     # path('edit-nilai-kriteria/<int:pk>/', views.edit_nilai_kriteria, name='edit-nilai-kriteria'),
     # path('delete-nilai-kriteria/<int:pk>/', views.delete_nilai_kriteria, name='delete-nilai-kriteria'),
     
     #Menu Supplier
     path('supplier/', views.view_supplier, name='view_supplier'),
     path('supplier/create', views.create_supplier, name = 'create-supplier'),
     path('edit-supplier/<int:pk>/', views.edit_supplier, name='edit-supplier'),
     path('delete-supplier/<int:pk>/', views.delete_supplier, name='delete-supplier'),
     
     #Menu calculation
     path('select_kriteria/', views.select_kriteria, name='select_kriteria'),
     path('calculation/', views.input_kriteria, name='input_kriteria'),
     path('calculation/result', views.result, name='result'),
     
]


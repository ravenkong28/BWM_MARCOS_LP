from django.urls import path
from . import views

urlpatterns = [
     path('perhitunganLP/', views.lp_perhitungan, name='lp_perhitungan'),
     path('result/', views.lp_result, name='lp_result'),
]


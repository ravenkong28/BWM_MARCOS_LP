from django.urls import path
from .views import PasswordsChangeView
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('login/', views.user_login, name='login'),
     path('register/', views.signUp, name='register'),
     path('logout/', LogoutView.as_view(), name='logout'),
     
     path('edit_profile/', views.EditProfile, name='edit_profile'),
     path('change-password/', views.PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='change_password'),
     path('change-password_success/', views.password_success, name='password_success'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
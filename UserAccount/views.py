from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import ProfileModel
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, LoginUserForm, ProfileUpdateForm


def user_login(request):
     if request.user.is_authenticated:
          return render(request, 'home.html', {'active_page': 'home'})
     else:
          if request.method == "POST":
               form = LoginUserForm(request, data=request.POST)
               

               if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')

                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                         login(request, user)
                         messages.success(request, f"You are logged in successfully as {user.first_name} {user.last_name}")
                         return redirect('home')
                    else:
                         messages.error(request, "Error")
               elif len(form.cleaned_data.get('password')) < 8:
                    messages.error(request, "Password must be at least 8 characters")
                    return redirect('login')
               else:
                    messages.error(request, "Username or password incorrect")

          else:
               form = LoginUserForm()

     return render(request, 'registration/login.html', {'form': form})


def signUp(request):
     if request.user.is_authenticated:
          return render(request, 'home.html', {'active_page': 'home'})
     else:
          if request.method == "POST":
               form = SignUpForm(request.POST)
               if form.is_valid():
                    user = form.save()
                    ProfileModel.objects.create(user=user)
                    
                    messages.success(request, "Your account is created successfully. Please log in.")
                    return redirect('login')
          else:
               form = SignUpForm()
          return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='/login')
def EditProfile(request):
     user = request.user
     if request.method == 'POST':
          user_form = EditProfileForm(request.POST, instance=user)
          profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profilemodel)

          if user_form.is_valid() and user_form.has_changed() and profile_form.is_valid() and profile_form.has_changed():
               user_form.save()
               messages.success(request, 'Profile updated successfully.')
               profile_form.save()
               messages.success(request, 'Profile Picture updated successfully.')
               return redirect('edit_profile')
          elif user_form.is_valid() and user_form.has_changed():
               user_form.save()
               messages.success(request, 'Profile updated successfully.')
          elif profile_form.is_valid() and profile_form.has_changed(): 
               profile_form.save()
               messages.success(request, 'Profile Picture updated successfully.')
          else :
               messages.error(request, 'New Profile Picture is required and must be in the format: png, jpg, jpeg.')
                    
          return redirect('edit_profile')
     else:
          user_form = EditProfileForm(instance=user)
          profile_form = ProfileUpdateForm(instance=user.profilemodel)

     return render(request, 'registration/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form, 'user': user})

@method_decorator(login_required(login_url='/login'), name='dispatch')
class PasswordsChangeView(PasswordChangeView):
     form_class = PasswordChangingForm
     success_url = reverse_lazy('password_success')

     def form_valid(self, form):
          response = super().form_valid(form)
          form.save()  
          messages.success(self.request, 'Password changed successfully.')
          return response


def password_success(request):
     return redirect('login')
     # return render(request, 'registration/login.html')

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel
# from BWM_MARCOS.models import Profile

class LoginUserForm(AuthenticationForm):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)

          self.fields['username'].widget.attrs.update({
               'class': 'form-control form-control-user',
               'placeholder': "Enter your username"
          })
          self.fields['password'].widget.attrs.update({
               'class': 'form-control',
               'placeholder': "Enter your password"
          })



class SignUpForm(UserCreationForm):
     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Your first name'}))
     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Your last name'}))
     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Username'}))
     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}))
     password1 = forms.CharField(widget=forms.PasswordInput)
     password2 = forms.CharField(widget=forms.PasswordInput)
     
     class Meta:
          model = User
          fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

     def clean_email(self):
          email = self.cleaned_data.get('email')
          if User.objects.filter(email=email).exists():
               raise forms.ValidationError('This email is already in use. Please use a different email address.')
          return email
     
     def clean_username(self):
          username = self.cleaned_data.get('username')
          if User.objects.filter(username=username).exists():
               raise forms.ValidationError('This username is already taken. Please choose a different username.')
          return username
     

     def __init__(self, *args, **kwargs):
          super(SignUpForm, self).__init__(*args, **kwargs)

          self.fields['password1'].widget.attrs['class'] = 'form-control'
          self.fields['password2'].widget.attrs['class'] = 'form-control'
          
class EditProfileForm(UserChangeForm):
     username = forms.CharField(
          max_length=100,
          widget=forms.TextInput(attrs={'class': 'form-control'}),
          disabled=True
     )
     email = forms.EmailField(
          widget=forms.EmailInput(attrs={'class': 'form-control'}),
          disabled=True
     )
     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

     class Meta:
          model = User
          fields = ['username', 'first_name', 'last_name', 'email']

     def clean_email(self):
          email = self.cleaned_data.get('email')
          existing_users = User.objects.exclude(email=self.instance.email)

          if existing_users.filter(email=email).exists():
               raise forms.ValidationError('This email is already in use. Please use a different email address.')
          return email

     def clean_username(self):
          username = self.cleaned_data.get('username')
          existing_users = User.objects.exclude(username=username)

          if existing_users.filter(username=username).exists():
               raise forms.ValidationError('This username is already taken. Please choose a different username.')
          return username

class ProfileUpdateForm(UserChangeForm):
     class Meta:
          model = ProfileModel
          fields = ['image']


          
          
class PasswordChangingForm(PasswordChangeForm):
     old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
     new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
     new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

     class Meta:
          model = User
          fields = ['old_password', 'new_password1', 'new_password2']

     def clean_old_password(self):
          old_password = self.cleaned_data.get('old_password')
          user = self.user
          if not user.check_password(old_password):
               raise forms.ValidationError("Your old password is incorrect.")
          return old_password
     
     def clean(self):
          cleaned_data = super().clean()
          new_password1 = cleaned_data.get('new_password1')
          new_password2 = cleaned_data.get('new_password2')

          if new_password1 and new_password2 and new_password1 != new_password2:
               raise forms.ValidationError("The new passwords do not match.")

          return cleaned_data

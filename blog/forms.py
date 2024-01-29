from django import forms
from .models import PostModel, Comment

class PostModelForm(forms.ModelForm):
     content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

     class Meta:
          model = PostModel
          fields = ['title', 'content']

     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field_name, field in self.fields.items():
               field.widget.attrs.update({'class': 'form-control'})


class PostUpdateForm(forms.ModelForm):
     content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

     class Meta:
          model = PostModel
          fields = ['title', 'content']

     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field_name, field in self.fields.items():
               field.widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
     content = forms.CharField(
          label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here....'}))

     class Meta:
          model = Comment
          fields = ('content',)
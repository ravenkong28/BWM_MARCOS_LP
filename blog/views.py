from django.shortcuts import render, redirect ,get_object_or_404
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login')
def index(request):
     posts = PostModel.objects.all()
     if request.method == 'POST':
          form = PostModelForm(request.POST)
          if form.is_valid():
               instance = form.save(commit=False)
               instance.author = request.user
               instance.save()
               return redirect('blog-index')
     else:
          form = PostModelForm()
     context = {
          'posts': posts,
          'form': form
     }

     return render(request, 'inner/blog/index.html', context)


@login_required(login_url='/login')
def post_detail(request, pk):
     post = PostModel.objects.get(id=pk)
     if request.method == 'POST':
          c_form = CommentForm(request.POST)
          if c_form.is_valid():
               instance = c_form.save(commit=False)
               instance.user = request.user
               instance.post = post
               instance.save()
               return redirect('blog-post-detail', pk=post.id)
     else:
          c_form = CommentForm()
     context = {
          'post': post,
          'c_form': c_form,
     }
     return render(request, 'inner/blog/post_detail.html', context)


@login_required(login_url='/login')
def post_edit(request, pk):
     post = PostModel.objects.get(id=pk)
     if request.method == 'POST':
          form = PostUpdateForm(request.POST, instance=post)
          if form.is_valid() and form.has_changed():
               form.save()
               messages.success(request, f"Post edited successfully")
          
          return redirect('blog-post-detail', pk=post.id)
     else:
          form = PostUpdateForm(instance=post)
     context = {
          'post': post,
          'form': form,
     }
     return render(request, 'inner/blog/post_edit.html', context)


@login_required(login_url='/login')
def post_delete(request, pk):
     post = PostModel.objects.get(id=pk)
     if request.method == 'POST':
          post.delete()
          messages.success(request, f"Post deleted successfully")
          return redirect('blog-index')
     context = {
          'post': post
     }
     return render(request, 'inner/blog/post_delete.html', context)



@login_required(login_url='/login')
def LikeView(request, pk):
     post = get_object_or_404(PostModel, id=pk)

     if post.likes.filter(id=request.user.id).exists():
          post.likes.remove(request.user)
     else:
          post.likes.add(request.user)

     return HttpResponseRedirect(reverse('blog-post-detail', args=[str(pk)]))


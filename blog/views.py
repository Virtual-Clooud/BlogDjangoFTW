from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import *
from better_auth.models import User
# Create your views here.
def CreateBlog(request):
	if request.method == 'POST':
		titulo = request.POST.get('titulo')
		texto = request.POST.get('texto')
		tagM = Tag.objects.all()
		tag = request.POST.get('tags')
		tags = tag.split(" ")
		
		novo_blog = Post(title=titulo, 
			text=texto, author= request.user)
		novo_blog.save()

		for x in range(len(tags)):
			if Tag.objects.filter(text=tags[x]):
					PostTagConnect(post = Post.objects.get(title=titulo), tag = Tag.objects.get(text=tags[x])).save()
			else:
					Tag(text = tags[x]).save()
					PostTagConnect(post = Post.objects.get(title=titulo), tag = Tag.objects.get(text=tags[x])).save()
				
		post = Post.objects.all()
		user = request.user
		print(tag.split(" "))
		return render(request, "blog/blog_view.html", {'post': post, 'user': user})

	else:
		post = Post.objects.all()
		user = request.user
		tag = Tag.objects.all()
		return render(request, "blog/create_blog.html", {'post': post, 'user': user,'tag': tag})
def BlogView(request):
	ptc = PostTagConnect.objects.get()
	tag = Tag.objects.all()
	if request.method == 'POST':
		title = request.POST.get('title_contains')
		if title == "":
			post = Post.objects.all()
		else:
			post = Post.objects.filter(title=title)
		
		user = request.user
		return render(request, "blog/blog_view.html", {'post': post, 'user': user, 'tag': tag})

	else:
		post = Post.objects.all()
		user = request.user
		return render(request, "blog/blog_view.html", {'post': post, 'user': user, 'tag': tag})
def PostDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)	
    if request.method == 'POST':
    	like = request.POST.get('like')
    	if like:
    		post.likes += 1
    		post.save()
    	else:
    		pass
    	return render(request, 'blog_detail.html', {'post': post})
    else:
    	return render(request, 'blog_detail.html', {'post': post})
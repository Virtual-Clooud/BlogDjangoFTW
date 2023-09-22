from django.shortcuts import render, redirect
from .models import *
from blog.models import Post
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def register(request):
	if request.method == 'POST':
		password = request.POST.get("password")
		email = request.POST.get("email")
		altura = float(request.POST.get("altura"))
		username = request.POST.get("username")
		novo_user = User(username=username, password= password, email=email,  altura=altura)
		novo_user.save()
		return redirect("accounts/login")

	else:
		return render(request, "better_auth/register.html")
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print(username)
		user = authenticate(request, email=username)
		print(user)
		if user is not None:
			login(request, user)
			messages.success(request, 'Login realizado com sucesso!')
			return redirect('pagina_inicial')  # Substitua 'pagina_inicial' pelo nome da sua página inicial
		else:
			messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')

			return render(request, 'better_auth/login.html')
	else:
		return render(request, "better_auth/login.html")
def user_page(request):
	user = request.user
	post = Post.objects.filter(author=user)
	return render(request, "better_auth/user_page.html", {'post': post})

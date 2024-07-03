from django.shortcuts import render, redirect, get_object_or_404
from firstblog.models import Post
from firstblog.forms import BlogForm, CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    blogs = Post.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

@login_required(login_url="my-login")
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

@login_required(login_url="my-login")
def update_blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'update_blog.html', {'form': form})

@login_required(login_url="my-login")
def delete_blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'delete_blog.html', {'blog': blog})

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("my-login")
        
    context = {'registerform':form}

    return render(request, 'firstblog/register.html', context=context)


def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    context = {'loginform': form}
    return render(request, 'firstblog/my-login.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect ('home')

@login_required(login_url='my-login')
def dashboard (request):
    return render(request, 'firstblog/dashboard.html')

from django.contrib import admin
from django.urls import path
from firstblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create_blog', views.create_blog, name='create_blog'),
    path('update_blog/<int:blog_id>', views.update_blog, name='update_blog'),
    path('delete_blog/<int:blog_id>', views.delete_blog, name='delete_blog'),
    path('register', views.register, name='register'),
    path('my-login', views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name='user-logout'),
]

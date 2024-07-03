from django.contrib import admin
from django.urls import path, include
from firstblog import views
from django.contrib.auth import views as auth_views

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
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url='/password_change/done/'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url='/password_reset/done/'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url='/reset/done/'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

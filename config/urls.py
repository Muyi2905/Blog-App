
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view (template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout, name='logout'),
    path('', include('blog.urls')),
]


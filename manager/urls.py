from django.contrib import admin
from django.urls import path
from manager import views
from .views import register_view, login_view, dashboard_view, add_view, logout_view, delete_view, update_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add/', views.add_view, name='add'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:id>/', views.delete_view, name='delete'), 
    path('update/<int:id>/', update_view, name='update'),    
]

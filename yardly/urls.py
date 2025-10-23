from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('jobs/', include('jobs.urls')),
    path('community/', include('community.urls')),
    path('feedback/', include('feedback.urls')),
    path('users/', include('users.urls')),
]

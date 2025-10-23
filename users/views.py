from django.shortcuts import render

def users_home(request):
    return render(request, 'users/index.html')

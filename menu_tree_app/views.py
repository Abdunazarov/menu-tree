from django.shortcuts import render

def home(request):
    return render(request, 'menu_tree_app/home.html')

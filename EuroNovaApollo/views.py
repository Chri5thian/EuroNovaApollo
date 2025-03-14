from django.shortcuts import render
from blog.models import Post


def home(request):
    
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

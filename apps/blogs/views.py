# Inside your app's views.py file
from django.shortcuts import render, redirect
from .models import Blog, Comment
# Pull the User class into the file

def index(request):
    context = {
    "blogs": Blog.objects.all()
    # Runs this SQL query, SELECT * FROM Blog
    }
    return render(request, 'blogs/index.html', context)

def blogs(request):
    # Using ORM
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    # Insert into blog (title, blog, created_at, updated_at) values (title, blog, NOW(), NOW() )
    return redirect('/')

def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog=blog)
    return redirect('/')

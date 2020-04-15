from django.shortcuts import render, get_object_or_404
from blog.models import blog

# Create your views here.


def allblog(request):
    my_blog = blog.objects
    return render(request, 'blog/blog.html', {'my_blog': my_blog})


def detail(request, blog_id):
    detail_blog = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blogs': detail_blog})

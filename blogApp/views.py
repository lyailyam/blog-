from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic
from .models import Post
from taggit.models import Tag


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def home_view(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    # Show most common tags
    common_tags = Post.tags.most_common()[:4]
    context = {
        'posts': posts,
        'common_tags': common_tags
    }
    return render(request, 'index.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'index.html', context)

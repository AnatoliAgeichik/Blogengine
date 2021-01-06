from django.shortcuts import render
from .forms import TagForm
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .models import Post, Tag
from .utils.objectDetailMixin import ObjectDetailMixin
def posts_list(request):
    posts=Post.objects.all()
    return render(request, 'blog/index.html', context={'posts':posts})

# def post_detail(request, slug):
#     post=Post.objects.get(slug__iexact=slug)
#     return render(request,'blog/post_detail.html', context={'post':post})

class PostDetail(ObjectDetailMixin,View):
    model = Post
    temlate = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin,View):
    model = Tag
    temlate ='blog/tag_detail.html'

class TagCreate(View):
    def get(self,request):
        form=TagForm()
        return render(request ,"blog/tag_create_html",context={'form':form})

def tags_list(request):
    tags=Tag.objects.all()
    return render(request,"blog/tags_list.html", context={'tags':tags})

# def tag_detail(request, slug):
#     tag=Tag.objects.get(slug__iexact=slug)
#     return render(request,'blog/tag_detail.html',context={'tag':tag})
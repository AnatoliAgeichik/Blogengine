from django.shortcuts import get_object_or_404
from django.shortcuts import render
#from blog.models import Post
class ObjectDetailMixin:
    model=None
    temlate=None

    def get(self,request,slug):
        obj=get_object_or_404(self.model,slug__iexact=slug)
        return render(request,self.temlate,context={self.model.__name__.lower():obj})



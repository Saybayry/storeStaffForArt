
from django.views import View, generic
from .models import productForArt
from django.shortcuts import render

# Create your views here.
class startPage(generic.ListView):
    model = productForArt
    template_name = "startPage.html"
    context_object_name = "productForArt_list"
    queryset = productForArt.objects.all()[:20]
def pageInwork(request, *args, **kwargs):
    return  render(request, "pageInwork.html", {})

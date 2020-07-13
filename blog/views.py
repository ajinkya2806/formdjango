from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import HttpResponse, Http404
from practice.forms import ContactForm

#Create your views here
def home_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context ={
        "title":"Contact form",
        "form": form
    }
    
    return render(request, "forms.html", context)


def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {"object":obj}
    return render(request, template_name, context)

def blog_post_list_view(request):
    return

def blog_post_rerieve_view(request):
    return

def blog_post_update_view(request):
    return

def blog_post_create_view(request):
    return


def blog_post_delete_view(request):
    return
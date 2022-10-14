from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from .forms import ContactForm

from .models import Category, Product


def index(request: HttpRequest):
    error = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'error'
    categories = Category.objects.all().order_by('name')
    products = Product.objects.filter(is_published=1).order_by('title')
    form = ContactForm()
    return render(
        request,
        'app/index.html',
        {
            'categories': categories,
            'products': products,
            'contact_form': form,
            'contact_error': error
        }
    )


# def email(request: HttpRequest):
#     return HttpResponse("email")


def error404(request: HttpRequest, exception):
    return HttpResponse("error404")

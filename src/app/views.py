from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models import Category, Product


@require_GET
def index(request: HttpRequest):
    categories = Category.objects.all().order_by('name')
    products = Product.objects.filter(is_published=1).order_by('title')
    return render(request, 'app/index.html', {'categories': categories, 'products': products}, status=200)


# def email(request: HttpRequest):
#     return HttpResponse("email")


def error404(request: HttpRequest, exception):
    return HttpResponse("error404")

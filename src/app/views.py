from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .forms import ContactForm

from .models import Category, Product


# def index(request: HttpRequest):
#     error = None
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             error = 'error'
#     categories = Category.objects.all().order_by('name')
#     products = Product.objects.filter(is_published=1).order_by('title')
#     form = ContactForm()
#     return render(
#         request,
#         'app/index.html',
#         {
#             'categories': categories,
#             'products': products,
#             'contact_form': form,
#             'contact_error': error
#         }
#     )


# def email(request: HttpRequest):
#     return HttpResponse("email")


def error404(request: HttpRequest, exception):
    return HttpResponse("error404")


class IndexView(View):
    template_name = "app/index.html"

    def get_context_data(self):
        categories = Category.objects.all().order_by('name')
        products = Product.objects.filter(is_published=1).order_by('title')
        form = ContactForm()
        content = {
            'categories': categories,
            'products': products,
            'contact_form': form,
            'contact_error': None
        }
        return content

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        form = ContactForm(request.POST)
        content = self.get_context_data()
        if form.is_valid():
            form.save()
        else:
            content['contact_error'] = 'Error'
        return render(request, self.template_name, content)


class ProductView(ListView):
    model = Product
    template_name = 'app/index.html'
    context_object_name = 'products'
    object_list = None

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(ProductView, self).get_context_data()
        categories = Category.objects.all().order_by('name')
        content.update({
            'categories': categories,
            'contact_form': ContactForm(),
            'contact_error': None
        })
        return content

    def post(self, request):
        form = ContactForm(request.POST)
        content = self.get_context_data()
        if form.is_valid():
            form.save()
        else:
            content['contact_error'] = 'Error'
        content['products'] = self.get_queryset()
        return render(request, self.template_name, content)

    def get_queryset(self):
        return Product.objects.filter(is_published=True).select_related('category')

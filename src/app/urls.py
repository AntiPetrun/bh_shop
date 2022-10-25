from django.urls import path
from .views import ProductView


urlpatterns = [
    path('', ProductView.as_view(), name='index'),
]

handler404 = 'app.views.error404'

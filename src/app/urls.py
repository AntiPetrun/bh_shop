from django.urls import path, register_converter, re_path
from .views import index
from django.conf.urls import handler404


# class YearConverter:
#     regex = '[0-9]{4}'
#
#     def to_python(self, value):
#         return int(value)
#
#     def to_url(self, value):
#         return str(value)
#
#
# register_converter(YearConverter, 'yyyy')

urlpatterns = [
    path('', index, name='categories'),
    # re_path(r'[0-9]{5}/', email),
]

handler404 = 'app.views.error404'

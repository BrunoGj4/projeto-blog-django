from django.urls import path
from .views import blog_index

app_name = 'blgo'

urlpatterns = [
    path('', blog_index, name='blog_index')
]
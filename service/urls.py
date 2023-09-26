from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page
from main.views import index, about, redirect_to_original

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cache_page(60**2)(index), name='index'),
    path('about/', cache_page(60**2)(about), name='about'),
    path('<slug:slug>/', redirect_to_original, name='redirect')
]

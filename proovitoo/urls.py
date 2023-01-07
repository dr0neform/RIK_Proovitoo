from django.template.defaulttags import url
from django.urls import path
from django.contrib import admin

from . import views


app_name = 'proovitoo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update=<str:reg_code>/', views.update, name='update'),
    path('detail=<str:reg_code>/', views.detail, name='detail'),
    path('reg_code_autocomplete/', views.reg_code_autocomplete, name='reg_code_autocomplete'),
    path('id_code_autocomplete/', views.id_code_autocomplete, name='id_code_autocomplete')

]
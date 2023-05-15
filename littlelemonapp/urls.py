from django.urls import path, re_path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
    #re_path(r'menu_item/?P<pk\d+)$', views.menu, name='menu_item'),
    #path('menu_item10', views.display_menu_item),
    #re_path(r' ^menu_item/[0-9]){2})/$', views.display_menu_item),
] 
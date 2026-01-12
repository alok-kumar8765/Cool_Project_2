from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-order/', views.create_order, name='create_order'),
    path('order-receipt/<int:order_id>/', views.order_receipt, name='order_receipt'),
    path('menu/', views.menu_crud, name='menu_crud'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('menu/edit/<int:item_id>/', views.edit_menu_item, name='edit_menu_item'),
    path('menu/delete/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
    path('search-order/', views.search_order, name='search_order'),
    path('all-orders/', views.all_orders, name='all_orders'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
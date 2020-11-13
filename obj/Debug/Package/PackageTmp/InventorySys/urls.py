from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from product_db import views   
from rest_framework.urlpatterns import format_suffix_patterns# add this
#router = routers.DefaultRouter()                      # add this
#router.register(r'products', views.productView, 'product')
#router.register(r'purchaseOrders', views.purchaseOrderView, 'purchase_order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.productList.as_view()),
    path('api/<int:pk>/', views.productDetail.as_view()),
]

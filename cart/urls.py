from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    # 카트 상세 페이지 URL 패턴
    path('', views.cart_detail, name='cart_detail'),
    # 카트에 제품 추가 URL 패턴
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    # 카트에서 제품 제거 URL 패턴
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
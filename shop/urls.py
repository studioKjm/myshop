from django.urls import path
from . import views

# 애플리케이션 이름 설정
app_name = 'shop'

# URL 패턴 정의
urlpatterns = [
    # 기본 제품 목록 페이지 URL 패턴
    path('', views.product_list, name='product_list'),
    # 카테고리별 제품 목록 페이지 URL 패턴
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # 제품 상세 페이지 URL 패턴
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
"""
URL configuration for 5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 관리자 사이트 URL 패턴
    path('admin/', admin.site.urls),
    # 카트 애플리케이션 URL 패턴 포함
    path('cart/', include('cart.urls', namespace='cart')),
    # 주문 애플리케이션 URL 패턴 포함
    path('orders/', include('orders.urls', namespace='orders')),
    # 상점 애플리케이션 URL 패턴 포함
    path('', include('shop.urls', namespace='shop')),
]

# 디버그 모드일 때 미디어 파일 서빙 설정
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
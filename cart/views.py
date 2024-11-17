from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    # 카트 객체를 초기화
    cart = Cart(request)
    # 제품 객체를 가져옴
    product = get_object_or_404(Product, id=product_id)
    # 폼 데이터를 CartAddProductForm으로 초기화
    form = CartAddProductForm(request.POST)
    # 폼이 유효한지 확인
    if form.is_valid():
        cd = form.cleaned_data
        # 카트에 제품을 추가
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    # 카트 상세 페이지로 리디렉션
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    # 카트 객체를 초기화
    cart = Cart(request)
    # 제품 객체를 가져옴
    product = get_object_or_404(Product, id=product_id)
    # 카트에서 제품을 제거
    cart.remove(product)
    # 카트 상세 페이지로 리디렉션
    return redirect('cart:cart_detail')

def cart_detail(request):
    # 카트 객체를 초기화
    cart = Cart(request)
    # 각 항목에 대해 수량 업데이트 폼을 초기화
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={'quantity': item['quantity'],
                                                 'override': True})
    # 카트 상세 페이지를 렌더링
    return render(request, 'cart/detail.html', {'cart': cart})
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product

def product_list(request, category_slug=None):
    # 선택된 카테고리를 초기화
    category = None
    # 모든 카테고리를 가져옴
    categories = Category.objects.all()
    # 사용 가능한 모든 제품을 필터링
    products = Product.objects.filter(available=True)
    # 카테고리 슬러그가 제공된 경우
    if category_slug:
        # 해당 카테고리를 가져옴
        category = get_object_or_404(Category, slug=category_slug)
        # 해당 카테고리에 속한 제품을 필터링
        products = products.filter(category=category)
    # 제품 목록 페이지를 렌더링
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    # 주어진 ID와 슬러그에 해당하는 제품을 가져옴
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    # 카트에 추가할 제품 폼을 초기화
    cart_product_form = CartAddProductForm()
    # 제품 상세 페이지를 렌더링
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
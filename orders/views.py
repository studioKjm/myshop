from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

def order_create(request):
    # 장바구니 객체 생성
    cart = Cart(request)
    if request.method == 'POST':
        # 폼 데이터로 OrderCreateForm 객체 생성
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # 폼 데이터가 유효하면 주문 저장
            order = form.save()
            for item in cart:
                # 장바구니의 각 항목을 OrderItem 객체로 생성
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # 장바구니 비우기
            cart.clear()
            # 비동기 작업 실행
            order_created.delay(order.id)
            # 주문 생성 완료 페이지 렌더링
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        # GET 요청 시 빈 폼 생성
        form = OrderCreateForm()
    # 주문 생성 페이지 렌더링
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
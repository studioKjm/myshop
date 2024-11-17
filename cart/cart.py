from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:
    def __init__(self, request):
        """
        카트를 초기화.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # 세션에 빈 카트를 저장
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        카트의 항목을 반복하고 데이터베이스에서 제품을 가져옴.
        """
        product_ids = self.cart.keys()
        # 제품 객체를 가져와 카트에 추가
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        카트의 모든 항목 수를 계산.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """
        카트에 제품을 추가하거나 수량을 업데이트.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # 세션을 modified로 표시하여 세션을 저장
        self.session.modified = True

    def remove(self, product):
        """
        카트에서 제품을 제거.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """
        카트 세션을 삭제.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def get_total_price(self):
        """
        카트의 총 가격을 계산.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
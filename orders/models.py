from django.db import models
from shop.models import Product

class Order(models.Model):
    # 주문자의 이름
    first_name = models.CharField(max_length=50)
    # 주문자의 성
    last_name = models.CharField(max_length=50)
    # 주문자의 이메일
    email = models.EmailField()
    # 주문자의 주소
    address = models.CharField(max_length=250)
    # 주문자의 우편번호
    postal_code = models.CharField(max_length=20)
    # 주문자의 도시
    city = models.CharField(max_length=100)
    # 주문 생성 시간
    created = models.DateTimeField(auto_now_add=True)
    # 주문 업데이트 시간
    updated = models.DateTimeField(auto_now=True)
    # 결제 여부
    paid = models.BooleanField(default=False)

    class Meta:
        # 생성 시간 기준으로 내림차순 정렬
        ordering = ('-created',)
        # 생성 시간에 인덱스 추가
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        # 주문 ID 반환
        return f'Order {self.id}'

    def get_total_cost(self):
        # 주문 항목의 총 비용 계산
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    # 주문과의 외래 키 관계 설정
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    # 제품과의 외래 키 관계 설정
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    # 제품 가격
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # 제품 수량
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        # 주문 항목 ID 반환
        return str(self.id)

    def get_cost(self):
        # 제품의 총 비용 계산
        return self.price * self.quantity
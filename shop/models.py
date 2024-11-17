from django.db import models
from django.urls import reverse

class Category(models.Model):
    # 카테고리 이름
    name = models.CharField(max_length=200)
    # 카테고리 슬러그 (고유 값)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        # 이름 기준으로 오름차순 정렬
        ordering = ('name',)
        # 슬러그 필드에 인덱스 추가
        indexes = [
            models.Index(fields=['slug'])
        ]
        # 관리자 페이지에서의 단수 이름
        verbose_name = 'category'
        # 관리자 페이지에서의 복수 이름
        verbose_name_plural = 'categories'

    def __str__(self):
        # 카테고리 이름 반환
        return self.name

    def get_absolute_url(self):
        # 카테고리의 절대 URL 반환
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    # 카테고리와의 외래 키 관계 설정
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # 제품 이름
    name = models.CharField(max_length=200)
    # 제품 슬러그
    slug = models.SlugField(max_length=200)
    # 제품 이미지
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # 제품 설명
    description = models.TextField(blank=True)
    # 제품 가격
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # 제품의 사용 가능 여부
    available = models.BooleanField(default=True)
    # 제품 생성 시간
    created = models.DateTimeField(auto_now_add=True)
    # 제품 업데이트 시간
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # 이름 기준으로 오름차순 정렬
        ordering = ('name',)
        # 여러 필드에 인덱스 추가
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        # 제품 이름 반환
        return self.name

    def get_absolute_url(self):
        # 제품의 절대 URL 반환
        return reverse('shop:product_detail', args=[self.id, self.slug])
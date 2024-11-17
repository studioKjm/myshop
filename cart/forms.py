from django import forms

# 제품 수량 선택을 위한 선택지 생성 (1부터 20까지)
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    # 수량 필드 정의, 선택지는 PRODUCT_QUANTITY_CHOICES를 사용하고 정수형으로 변환
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    # 수량 덮어쓰기 여부를 위한 필드 정의, 기본값은 False, HiddenInput 위젯 사용
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
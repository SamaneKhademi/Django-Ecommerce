from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم و فامیل'}),
                            required=True)
    shipping_email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
                            required=True)
    shipping_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس 1'}),
                            required=True)
    shipping_address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس 2'}),
                            required=False)
    shipping_city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'}),
                            required=True)
    shipping_state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'منطقه'}),
                            required=False)
    shipping_zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کدپستی'}),
                            required=False)
    shipping_country = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'}),
                            required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']

        exclude = ['user']


class PaymentForm(forms.Form):
    card_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم'}),
                            required=True)
    card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره کارت'}),
                            required=True)
    card_exp_date = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تاریخ انقضا'}),
                            required=True)
    card_cvv2_number = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cvv2'}),
                            required=True)
    card_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس 1'}),
                            required=True)
    card_address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس 2'}),
                            required=False)
    card_city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'}),
                            required=True)
    card_state = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'منطقه'}),
                            required=False)
    card_zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کدپستی'}),
                            required=True)
    card_country = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'}),
                            required=True)

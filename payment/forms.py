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
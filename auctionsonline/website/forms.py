from django import forms
from .models import Product, Auction


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=45)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=45)
    password2 = forms.CharField(max_length=45)
    firstname = forms.CharField(max_length=56)
    lastname = forms.CharField(max_length=45)
    cellphone = forms.CharField(max_length=45)
    address = forms.CharField(max_length=255)
    town = forms.CharField(max_length=45)
    postcode = forms.CharField(max_length=45)
    country = forms.CharField(max_length=45)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45)


class TopUpForm(forms.Form):
    amount = forms.DecimalField(max_digits=6, decimal_places=2)


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'image', 'description', 'quantity', 'category']

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['product_id', 'number_of_bids', 'time_starting', 'time_ending']
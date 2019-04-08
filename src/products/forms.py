from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	description = forms.CharField(
					required=True,
					widget=forms.Textarea(
						attrs={
							"placeholder": "Your description",
							"class": "new-class-name two",
							"id": "my-id-for-textarea",
							"rows":20,
							"cols": 120
						}
					)
				)
	price = forms.DecimalField(initial=9.99)
	class Meta():
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

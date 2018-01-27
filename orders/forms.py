from django.forms import ModelForm, Textarea, TextInput
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name','phone','note']
        widgets = {
            'name':TextInput(attrs={'class':'input'}),
            'phone':TextInput(attrs={'class':'input js-phone-mask', 'pattern':'.{19}'}),
            'note':Textarea(attrs={'class':'textarea','rows':'1','placeholder':'Необязательное поле'})
        }


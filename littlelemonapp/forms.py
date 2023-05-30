from django import forms
from .models import MyForm

# class UserForm(ModelForm):
#     class Meta:
#         model = Booking
#         fields = "__all__"

# class MyForm(forms.Form):
#     name = forms.CharField(label="Enter your name")
#     email = forms.EmailField(label="Enter your E-mail")
#     reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    #age = forms.IntegerField(label="Enter your age")
    #comment = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))

class myForm(forms.ModelForm):
    class LittleLemon:
        model = MyForm
        fiels = '__all__'
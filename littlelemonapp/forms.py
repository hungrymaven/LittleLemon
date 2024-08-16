from django import forms
from .models import Reserve

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

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = "__all__"
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
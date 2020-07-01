from django import forms


class AdvertForm(forms.Form):
    link = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Link"
        })
    )

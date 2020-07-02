from django import forms

PAGE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '6'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7')
]


class AdvertForm(forms.Form):
    link = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Car Search Link"
        })
    )
    page_choice = forms.IntegerField(
        label='In how many pages do you want to analyze ?',
        widget=forms.Select(attrs={
            "class": "btn btn-warning dropdown-toggle",
            "data-toggle": "dropdown",
            "aria-haspopup": "true",
            "aria-expanded": "false",
            "data-offset": "10,20"
        }, choices=PAGE_CHOICES))

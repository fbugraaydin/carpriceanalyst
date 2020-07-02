from django import forms

PAGE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '6'),
    ('5', '5'),
    ('4', '6'),
    ('4', '7'),
    ('4', '8'),
    ('4', '9'),
    ('4', '10'),
    ('4', '11'),
    ('4', '12'),
    ('4', '13'),
    ('4', '14'),
    ('4', '15')
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

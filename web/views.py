from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import AdvertForm


def index(request):
    form = AdvertForm()
    if request.method == 'POST':
        form = AdvertForm(request.POST)
        if form.is_valid():
            return render(request, 'index.html', {'message': '{link}'.format(link=form.cleaned_data['link']), "form": form})

    return render(request, 'index.html', {'message': 'Welcome for Car Analysis', "form": form})

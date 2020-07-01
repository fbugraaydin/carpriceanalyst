from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import AdvertForm
from .fromowner import get_adverts_by_url,calculate_total_amount


def index(request):
    form = AdvertForm()
    if request.method == 'POST':
        form = AdvertForm(request.POST)
        if form.is_valid():
            total_adverts = get_adverts_by_url(form.cleaned_data['link'])
            total_amount = calculate_total_amount(total_adverts)
            average_amount = "{:,.3f} TL".format(float(total_amount/len(total_adverts)))
            return render(request, 'index.html',
                          {'average_amount': 'Average Price is {average_amount} '.format(average_amount=average_amount),
                           "form": form})

    return render(request, 'index.html', {'message': 'Welcome for Car Analysis', "form": form})

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import AdvertForm
from .fromowner import get_adverts_by_url, calculate_total_amount
from .util import *
import datetime


statistic = dict()


def index(request):
    form = AdvertForm()
    if request.method == 'POST':
        form = AdvertForm(request.POST)
        if form.is_valid():
            total_adverts = get_adverts_by_url(form.cleaned_data['link'], form.cleaned_data['page_choice'])
            total_amount = calculate_total_amount(total_adverts)
            average_amount = float(total_amount / len(total_adverts))
            format_average_amount = "{:,.3f} TL".format(average_amount)
            today = format_time(datetime.datetime.now())
            statistic[today] = average_amount

            return render(request, 'index.html',
                          {'average_amount': 'Average Price is {average_amount} '.format(
                              average_amount=format_average_amount),
                              "form": form,
                              'data': list(statistic.values()),
                              'labels': list(statistic.keys())})

    return render(request, 'index.html', {"form": form})

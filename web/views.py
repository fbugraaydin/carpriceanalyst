from django.shortcuts import render
from .forms import AdvertForm
from .util import *
from django.http import JsonResponse
from .analyzer import *


def index(request):
    form = AdvertForm()
    url_list = Link.objects.values_list('link', flat=True)
    if request.method == 'POST':

        if request.POST.get('selected_url') is not None:
            input_link = request.POST['selected_url']

            average_amount_list, date_list = flat_values(input_link)

            return JsonResponse({"data": list(average_amount_list),
                                 "labels": list(map(lambda d: format_date(d), date_list))}, status=200)

        elif request.POST.get('link') is not None and request.POST.get('page_choice') is not None:
            input_link = request.POST['link']
            input_page_choice = int(request.POST['page_choice'])

            average_amount = analyze(input_link, input_page_choice)
            save(average_amount, input_link)

            average_amount_list, date_list = flat_values(input_link)

            format_average_amount = "{:,.3f} ₺".format(average_amount)
            return JsonResponse({'average_amount': 'Average Price is {average_amount} '.format(
                average_amount=format_average_amount),
                'data': list(average_amount_list),
                'labels': list(map(lambda d: format_date(d), date_list))}, status=200)

    return render(request, 'index.html', {"form": form, "url_list": url_list})


def history_list(request):
    url_list = Link.objects.values_list('link', flat=True)
    return JsonResponse(list(url_list), status=200, content_type='application/json',safe=False)


def flat_values(input_link):
    average_amount_list = Statistic.objects.filter(
        link__link=input_link).values_list('average_amount', flat=True)
    date_list = Statistic.objects.filter(link__link=input_link).values_list('date', flat=True)
    return average_amount_list, date_list

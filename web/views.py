from django.shortcuts import render
from .forms import AdvertForm
from .analyzer import get_adverts_by_url, calculate_total_amount
from .util import *
from datetime import date, timedelta
from .models import *
from django.http import JsonResponse
import logging

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def index(request):
    form = AdvertForm()
    url_list = Link.objects.values_list('link', flat=True)
    if request.method == 'POST':

        if request.POST.get('selected_url') is not None:
            input_link = request.POST['selected_url']
            average_amount_list = Statistic.objects.filter(
                link__link=input_link).values_list('average_amount', flat=True)
            date_list = Statistic.objects.filter(link__link=input_link).values_list('date', flat=True)

            return JsonResponse({"data": list(average_amount_list),
                                 "labels": list(map(lambda d: format_date(d), date_list))}, status=200)

        elif request.POST.get('link') is not None and request.POST.get('page_choice') is not None:
            input_link = request.POST['link']
            input_page_choice = int(request.POST['page_choice'])

            logger.info('Link : {link}, page_choice: {page_choice}'.format(link=input_link, page_choice=input_page_choice))

            total_adverts = get_adverts_by_url(input_link, input_page_choice)
            total_amount = calculate_total_amount(total_adverts)
            average_amount = float(total_amount / len(total_adverts))
            format_average_amount = "{:,.3f} TL".format(average_amount)
            today = date.today()

            link = Link.objects.filter(link=input_link)
            if link is None or len(link) == 0:
                link = Link(link=input_link)
                link = link.save()

            statistic = Statistic.objects.filter(date=today, link__link=input_link)
            if len(statistic) == 1:
                statistic.update(average_amount=average_amount)
            else:
                statistic = Statistic(date=today, link=link[0], average_amount=average_amount)
                statistic.save()

            average_amount_list = Statistic.objects.filter(
                link__link=input_link).values_list('average_amount', flat=True)
            date_list = Statistic.objects.filter(link__link=input_link).values_list('date', flat=True)

            return JsonResponse({'average_amount': 'Average Price is {average_amount} '.format(
                average_amount=format_average_amount),
                'data': list(average_amount_list),
                'labels': list(map(lambda d: format_date(d), date_list))}, status=200)

    return render(request, 'index.html', {"form": form, "url_list": url_list})

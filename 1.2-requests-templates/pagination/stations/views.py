import csv
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    path = settings.BUS_STATION_CSV
    page_number = int(request.GET.get('page', 1))

    with open(path, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        pagi_list = []
        for row in reader:
            pagi_list.append(row)
        paginator = Paginator(pagi_list, 10)
        page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

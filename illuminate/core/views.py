from django.shortcuts import render

import requests

from .models import Office, AccessToken

AIESEC_INTERNATIONAL_ID = 1626
REGIONAL_IDS = [1632, 1630, 1627, 1629]


def index(request):
    # AIESEC INTERNATIONAL
    AIESEC_INTERNATIONAL = Office.objects.get(pk=1626)

    # REGIONS
    MIDDLE_EAST_AND_AFRICA = Office.objects.get(pk=1632)
    ASIA_PACIFIC = Office.objects.get(pk=1630)
    AMERICAS = Office.objects.get(pk=1627)
    EUROPE = Office.objects.get(pk=1629)

    # Egypt
    EGYPT = Office.objects.get(pk=1609)
    egypt_lcs = Office.objects.filter(parent_office=EGYPT).order_by('name')

    countries_offices = Office.objects.filter(parent_office=MIDDLE_EAST_AND_AFRICA) | Office.objects.filter(
        parent_office=ASIA_PACIFIC) | Office.objects.filter(parent_office=AMERICAS) | Office.objects.filter(
        parent_office=EUROPE)
    countries_offices = countries_offices.order_by('name')

    table_headers = ['Rank', 'iGV', 'iGT', 'iGE', 'oGV', 'oGT', 'oGE', 'Total']

    context_dictionary = {'AIESEC_INTERNATIONAL': AIESEC_INTERNATIONAL,
                          'MIDDLE_EAST_AND_AFRICA': MIDDLE_EAST_AND_AFRICA,
                          'ASIA_PACIFIC': ASIA_PACIFIC,
                          'AMERICAS': AMERICAS,
                          'EUROPE': EUROPE,
                          'egypt_lcs': egypt_lcs,
                          'countries_offices': countries_offices,
                          'table_headers': table_headers,
                          }
    return render(request, 'core/index.html', context_dictionary)


def update_offices(request):
    access_token, created = AccessToken.objects.get_or_create(id=1)
    if created:
        access_token.save()

    url = 'https://gis-api.aiesec.org/v2/committees.json?access_token=' + access_token.value + '&per_page=500'
    r = requests.get(url).json()

    for i in range(1, r['paging']['total_pages'] + 1):
        url = 'https://gis-api.aiesec.org/v2/committees.json?access_token=' + access_token.value + '&per_page=500' + '&page=' + str(
            i)
        r = requests.get(url).json()
        parse_data(r)

    return render(request, 'core/index.html', {})

def request_office(id):
    access_token, created = AccessToken.objects.get_or_create(id=1)
    if created:
        access_token.save()

    url = 'https://gis-api.aiesec.org/v2/committees/' + str(id) + '.json?access_token=' + access_token.value
    r = requests.get(url).json()
    return r


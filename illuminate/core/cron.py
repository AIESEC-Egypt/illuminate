import re
import subprocess
import time

import requests
from django_cron import CronJobBase, Schedule
from . import create_token
from config.settings import base
from .models import AccessToken, Office


class UpdateAccessToken(CronJobBase):
    RUN_EVERY_MINS = 1 if base.DEBUG else 60  # 6 hours when not DEBUG

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'core.UpdateAccessToken'

    def do(self):
        self.create_token()

    def create_token(self):
        gis = create_token.GIS()
        access_token, created = AccessToken.objects.get_or_create(id=1)
        access_token.value = gis.generate_token('mohammed.hammad@aiesec.net', 'Meraki77')
        access_token.save()


class UpdateOffices(CronJobBase):
    RUN_EVERY_MINS = 1 if base.DEBUG else 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'core.UpdateOffices'

    def do(self):

        access_token, created = AccessToken.objects.get_or_create(id=1)
        if created:
            access_token.save()

        url = 'https://gis-api.aiesec.org/v2/committees.json?access_token=' + access_token.value
        r = requests.get(url).json()

        for i in range(1, r['paging']['total_pages'] + 1):
            url = 'https://gis-api.aiesec.org/v2/committees.json?access_token=' + access_token.value + \
                  '&page=' + str(i)
            r = requests.get(url).json()
            parse_data(r)

        print('done')


def parse_data(offices):
    print(len(offices['data']))
    for office_entry in offices['data']:
        child_office = update_specific_office(office_entry['id'],
                                              office_entry['name'],
                                              office_entry['tag'])

        if 'parent' in office_entry:
            if not (office_entry['parent'] == "null"):
                parent_office = update_specific_office(office_entry['parent']['id'],
                                                       office_entry['parent']['name'],
                                                       office_entry['parent']['tag'])
                child_office.parent_office = parent_office
                child_office.save()


def update_specific_office(id, name, tag):
    office, created = Office.objects.get_or_create(pk=id,
                                                   name=name)
    if tag == 'MC':
        office.entity_type = 'MC'
    elif tag == 'Region':
        office.entity_type = 'RE'
    elif tag == 'AI':
        office.entity_type = 'AI'
    elif tag == 'LC':
        office.entity_type = 'LC'
    else:
        office.entity_type = 'XX'
    office.save()
    return office


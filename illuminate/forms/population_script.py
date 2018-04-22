from illuminate.illuminate.forms.create_token import GIS
from illuminate.illuminate.forms.models import *

import requests


def delete_everything():

    Position.objects.all().delete()
    print("Positions Deleted")
    Role.objects.all().delete()
    print("Roles Deleted")
    Office.objects.all().delete()
    print("Offices Deleted")
    Standard.objects.all().delete()
    print("Standards Deleted")


def populate_standards():

    Standard(name='Personal Goal Setting', number='1').save()
    Standard(name='Outgoing Preparation Seminar', number='2').save()
    Standard(name='Expectation Setting', number='3').save()
    Standard(name='Incoming Preparation Seminar', number='4').save()
    Standard(name='Development Spaces', number='5').save()
    Standard(name='Debrief With AIESEC Home', number='6').save()
    Standard(name='Visa And Work Permit Information', number='7').save()
    Standard(name='Arrival Pickup', number='8').save()
    Standard(name='Departure Support', number='9').save()
    Standard(name='Job Description Information', number='10').save()
    Standard(name='Duration', number='11').save()
    Standard(name='Working Hours', number='12').save()
    Standard(name='First Day of Work', number='13').save()
    Standard(name='Insurance', number='14').save()
    Standard(name='Accommodation', number='15').save()
    Standard(name='Basic Living Cost', number='16').save()

    print("Standards Populated")


def populate_positions():

    Position(name='MCP').save()
    Position(name='MCVP').save()
    Position(name='LCP').save()
    Position(name='LCVP').save()
    Position(name='NST').save()
    Position(name='Team Leader').save()
    Position(name='Coordinator').save()
    Position(name='Member').save()
    print("Positions Populated")


def populate_role():

    Role(name='IGV').save()
    Role(name='IGE').save()
    Role(name='IGT').save()
    Role(name='OGV').save()
    Role(name='OGE').save()
    Role(name='OGT').save()
    Role(name='F&L').save()
    Role(name='TM').save()
    Role(name='IM').save()
    Role(name='Marketing').save()
    Role(name='PD').save()
    print("Roles Populated")


def populate_offices():
    print("Populaing Offices...")
    id = "1609"
    call = GIS()
    access_token = call.generate_token()
    print(access_token)
    url = 'https://gis-api.aiesec.org/v2/committees/' + id + '.json?access_token=' + access_token
    r = requests.get(url).json()
    for i in range(0, 23):
        name = r['suboffices'][i]['name']
        office_id = r['suboffices'][i]['id']
        Office(office_name=name).save()
        Office(office_id=office_id).save()
    print("Offices Populated")


def populate_all():

    populate_role()
    populate_positions()
    populate_offices()
    populate_standards()




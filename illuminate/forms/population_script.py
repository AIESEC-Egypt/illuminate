from illuminate.forms.create_token import GIS
from illuminate.forms.models import *
import requests


def delete_everything():

    Position.objects.all().delete()
    print("Positions Deleted")
    Role.objects.all().delete()
    print("Roles Deleted")
    Offices.objects.all().delete()
    print("Offices Deleted")


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
        name =r['suboffices'][i]['name']
        Offices(name=name).save()
    print("Offices Populated")


def populate_all():

    delete_everything()
    populate_role()
    populate_positions()




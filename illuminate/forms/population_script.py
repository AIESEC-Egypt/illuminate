from .create_token import GIS
from .models import *
import requests


def populate_positions():
    Position(name='MCP').save()
    Position(name='MCVP').save()
    Position(name='LCP').save()
    Position(name='LCVP').save()
    Position(name='NST').save()
    Position(name='Team Leader').save()
    Position(name='Coordinator').save()
    Position(name='Member').save()


def populate_role(name):
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


def populate_offices():
    id = "1609"
    call = GIS()
    access_token = call.generate_token()
    url = 'https://gis-api.aiesec.org/v2/committees/' + id + '.json?access_token=' + access_token
    r = requests.get(url).json()
    for i in range(0, 23):
        name =r['suboffices'][i]['name']
        Offices(name=name).save()


#tuple call
    # output = []
    # for i in range(0, 23):
    #     i = [(r['suboffices'][i]['id']), (r['suboffices'][i]['name'])]
    #     output.append(tuple(i))
    # LCS = tuple(output)
    # return LCS


populate_offices()
populate_positions()
populate_role()

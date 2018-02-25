from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Request(models.Model):
    HOST_LC_CHOICE=(
        ('6TH OCTOBER', '6TH OCTOBER'), ('AAST Alexandria', 'AAST Alexandria'),
        ('AAST In CAIRO', 'AAST In CAIRO'), ('Ain Shams University', 'Ain Shams University'),
        ('Alexandria', 'Alexandria'), ('Assiut', 'Assiut'),
        ('Beni Suef', 'Beni Suef'), ('Cairo University', 'Cairo University'),
        ('Damietta', 'Damietta'), ('Fayoum', 'Fayoum'),
        ('GUC', 'GUC'), ('Helwan', 'Helwan'),
        ('Luxor & Aswan', 'Luxor & Aswan'), ('Mansoura', 'Mansoura'),
        ('Menofia', 'Menofia'), ('Minya', 'Minya'),
        ('MIU', 'MIU'), ('New Cairo', 'New Cairo'),
        ('Sohag', 'Sohag'), ('Suez', 'Suez'),
        ('Tanta', 'Tanta'), ('Zagazig', 'Zagazig'),
    )

    POSITION_CHOICE=(
        ('MCP','MCP'),('MCVP','MCVP'),
        ('LCP','LCP'),('LCVP','LCVP'),
        ('Team Leader','Team Leader'),('Coordinator','Coordinator'),
        ('Member','Member'),
    )

    ROLE_CHOICE=(
        ('IGV','IGV'),('IGE','IGE'),('IGT', 'IGT'),
        ('OGV','OGV'),('OGE','OGE'),('OGT','OGT'),
        ('F&L', 'F&L'),('TM','TM'),('Marketing','Marketing'),
    )

    STEP_CHOICE=(
        ('Approval', 'Approval'),
        ('Realization', 'Realization'),
    )

    PROGRAM_CHOICE=(
        ('GV','Global Volunteer'),
        ('GE','Global Entrepreneur'),
        ('GT', 'Global Talent')
    )
    #Request filler info
    full_name = models.CharField(max_length=128, blank=False, null=False, help_text="Enter Your Full Name.")
    lc = models.CharField(max_length=1, blank=False, null=True, choices=HOST_LC_CHOICE)
    position = models.CharField(max_length=1, blank=False, null=True, choices=POSITION_CHOICE)
    role = models.CharField(max_length=1, blank=True, null=True, choices=ROLE_CHOICE)

    #EP info
    ep_name = models.CharField(max_length=128, blank=False, null=False, help_text="Enter EP's Full Name.")
    ep_entity = CountryField(blank=False,null=True, blank_label='Select Sending entity')
    #whatsapp_number = models. BigIntegerField(blank=False, null=False, help_text="Enter the number with country code.")
    ep_email = models.EmailField()
    ep_lc = models.CharField(max_length=1, blank=False, null=True, choices=HOST_LC_CHOICE)
    ep_id = models.IntegerField(blank=False, null=False, help_text="Enter EP ID.")
    opp_id = models.IntegerField(blank=False, null=False, help_text="Enter Opportunity ID.")

    #Request
    requested_break = models.CharField(max_length=1, blank=False, null=True, choices=STEP_CHOICE)
    program = models.CharField(max_length=1, blank=False, null=True, choices=PROGRAM_CHOICE)
    request_Reason = models.TextField(blank=False, null=False, help_text="Detailed yet to the point for us to help you best!")

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email


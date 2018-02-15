from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Complaint(models.Model):
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
    country_name_choice=(

    )
    PROGRAM_CHOICE=(
        ('GV','Global Volunteer'),
        ('GE','Global Entrepreneur'),
        ('GT', 'Global Talent')
    )

    full_name = models.CharField(max_length=128, blank=False, null=False, help_text="Enter Your Full Name.")
    whatsapp_number = models. BigIntegerField(blank=False, null=False, help_text="Enter the number with country code.")
    email = models.EmailField()
    country = CountryField(blank=False,null=True, blank_label='Select home country')
    program = models.CharField(max_length=1, blank=False, null=True, choices=PROGRAM_CHOICE)
    host_lc = models.CharField(max_length=1, blank=False, null=True, choices=HOST_LC_CHOICE)
    complaint = models.TextField(blank=False, null=False, help_text="Detailed yet to the point for us to help you best!")
    #image_upload = ImageField(upload_to=None, blank=True, help_text="Kindly add n some images if available!")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email


from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField

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

    PROGRAM_CHOICE=(
        ('GV','Global Volunteer'),
        ('GE','Global Entrepreneur'),
        ('GT', 'Global Talent')
    )

    TAG_CHOICE=(
        ('Accomodation','Accomodation'),('Job Description','Job Description'),
        ('Other','Other'),
    )

    full_name = models.CharField(max_length=128, blank=False, null=False, help_text="Enter Your Full Name.")
    whatsapp_number = models. BigIntegerField(blank=False, null=False, help_text="Enter the number with country code.")
    email = models.EmailField()
    country = CountryField(blank=False,null=True, blank_label='Select home country')
    program = models.CharField(max_length=1, blank=False, null=True, choices=PROGRAM_CHOICE)
    host_lc = models.CharField(max_length=1, blank=False, null=True, choices=HOST_LC_CHOICE)
    complaint = models.TextField(blank=False, null=False, help_text="Detailed yet to the point for us to help you best!")
    complaint_tag = MultiSelectField(max_length=1, blank=False, null=True, choices=TAG_CHOICE)
    #image_upload = ImageField(upload_to=None, blank=True, help_text="Kindly add n some images if available!")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email


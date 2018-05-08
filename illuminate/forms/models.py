from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField


# Population script filled choice models:

class Position(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Standard(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Office(models.Model):
    office_name = models.CharField(max_length=128, primary_key=True)
    office_id = models.IntegerField(blank=True, null=True)
    office_contact_name = models.CharField(max_length=128, blank=True, null=True)
    office_contact_email = models.EmailField(blank=True, null=True)
    office_contact_phone = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.office_name


# Main Models

class Filler(models.Model):
    filler_name = models.CharField(max_length=128, blank=True, null=True, help_text="Enter Your Full Name.")
    filler_email = models.EmailField(blank=True, null=True)
    filler_lc = models.ForeignKey(Office, null=True, blank=True, on_delete=models.CASCADE)
    filler_position = models.ForeignKey(Position, null=True, blank=True, on_delete=models.CASCADE)
    filler_role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.filler_name


class Ep(models.Model):
    # Required
    ep_name = models.CharField(max_length=128, blank=True, null=True, help_text="Enter Your Full Name.")
    ep_number = models.BigIntegerField(blank=True, null=True, help_text="Enter the number with country code.")
    ep_email = models.EmailField(blank=True, null=True)
    ep_host_lc = models.ForeignKey(Office, null=True, blank=True, on_delete=models.CASCADE)

    ep_country = CountryField(blank=True, null=True, blank_label='Select home country')
    ep_expa_id = models.IntegerField(blank=True, null=True, help_text="Enter EP ID.")
    opp_id = models.IntegerField(blank=True, null=True, help_text="Enter Opportunity ID.")

    ep_lc = models.CharField(max_length=128, blank=True, null=True, help_text="Enter lc Name.")

    def __str__(self):
        return self.ep_name


class Ticket(models.Model):
    PROGRAM_CHOICE = (('1', 'Global Volunteer'),
                      ('2', 'Global Talent'),
                      ('5', 'Global Entrepreneur'))

    STEP_CHOICE = (('Approval', 'Approval'),
                   ('Realization', 'Realization'))

    TAG_CHOICE = (('Accomodation', 'Accomodation'), ('Job Description', 'Job Description'),
                  ('Other', 'Other'),)
    TICKET_STATE_CHOICE = (('Open', 'Open'), ('In Progress', 'In Progress'),
                            ('Closed', 'Closed'))

    ticket_type = models.CharField(max_length=128, blank=False, null=True)  # complaint or Request
    ticket_state = models.CharField(max_length=128, blank=True, null=True, choices=TICKET_STATE_CHOICE)  # open, in-progress, closed
    comments = models.TextField(blank=True, null=True)
    program = models.CharField(max_length=1, blank=False, null=True, choices=PROGRAM_CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    ep = models.OneToOneField(Ep, on_delete=models.CASCADE, null=True, blank=True)
    filler = models.OneToOneField(Filler, on_delete=models.CASCADE, null=True, blank=True)

    # complaint
    complaint = models.TextField(blank=False, null=True, help_text="Detailed yet to the point for us to help you best!")
    complaint_type = models.CharField(max_length=128, blank=False, null=True)  # OGX if egypt else = ICX
    complaint_tag = MultiSelectField(max_length=128, blank=False, null=True, choices=TAG_CHOICE)
    complaint_solution = models.TextField()  # solution if complaint is solved
    # image_upload = ImageField(upload_to=None, blank=True, help_text="Kindly add some images if available!")  --STILL NEEDS WORK--

    # Request
    requested_break = models.CharField(max_length=128, blank=False, null=True, choices=STEP_CHOICE)
    request_Reason = models.TextField(blank=False, null=True, help_text="Detailed yet to the point for us to help you best!")

    #case
    case_mail_subject = models.CharField(max_length=128, blank=False, null=True)
    case_brief = models.TextField(blank=False, null=True, help_text="Detailed yet to the point")
    standards = models.ManyToManyField(Standard, null=True, blank=True,)

    def __str__(self):
        return self.ticket_type

from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from illuminate.users.models import User
from illuminate.core.unique_sluggify import unique_slugify
import datetime
import os
from uuid import uuid4

from django.utils import timezone


# Population script filled choice models:

class Position(models.Model):
    name = models.CharField(max_length=128)

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
    slug = models.SlugField()

    def save(self, **kwargs):
        slug = '%s' % (self.office_name)
        unique_slugify(self, slug)  ## from http://djangosnippets.org/snippets/1321/
        super(Office, self).save()

    def __str__(self):
        return self.office_name

# Functions

def path_and_rename(instance, filename):
    upload_to = 'Uploads/process_files/{}/{}'.format(datetime.date.today(), instance.pk)
    ent, ext = filename.split('.')
    # get filename
    if instance.pk:
        filename = '{}-{}.{}'.format(ent, instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}-{}.{}'.format(ent, uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

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
    TICKET_TYPE_CHOICE = (('Complaint', 'Complaint'),
                          ('Request', 'Request'),
                          ('Case', 'Case'))
    TICKET_STATE_CHOICE = (('Draft', 'Draft'),
                           ('Open', 'Open'),
                           ('In Progress', 'In Progress'),
                           ('Closed', 'Closed'))
    STANDARDS_CHOICE = (('#1', 'Personal Goal Setting'),
                        ('#2', 'Outgoing Preparation Seminar'),
                        ('#3', 'Expectation Setting'),
                        ('#4', 'Incoming Preparation Seminar'),
                        ('#5', 'Development Spaces'),
                        ('#6', 'Debrief With AIESEC Home'),
                        ('#7', 'Visa And Work Permit Information'),
                        ('#8', 'Arrival Pickup'),
                        ('#9', 'Departure Support'),
                        ('#10', 'Job Description Information'),
                        ('#11', 'Duration'),
                        ('#12', 'Working Hours'),
                        ('#13', 'First Day of Work'),
                        ('#14', 'Insurance'),
                        ('#15', 'Accommodation'),
                        ('#16', 'Basic Living Cost'))
    PROGRAM_CHOICE = (('1', 'Global Volunteer'),
                      ('2', 'Global Talent'),
                      ('5', 'Global Entrepreneur'))
    STEP_CHOICE = (('Approval', 'Approval'),
                   ('Realization', 'Realization'))
    COMPLAINT_OUTCOME_CHOICE = (('Solved', 'Solved'),
                                ('Not Solved', 'Not Solved'))
    REQUEST_OUTCOME_CHOICE = (('Confirmed', 'Confirmed'),
                              ('Not Confirmed', 'Not Confirmed'))
    CASE_OUTCOME_CHOICE = (('Won', 'Won'),
                           ('Lost', 'Lost'))
    CURRENCY_CHOICE = (('USD', 'USD'),
                       ('EGP', 'EGP'),
                       ('EUR', 'EUR'))

    ticket_type = models.CharField(max_length=128, blank=False, null=True, choices=TICKET_TYPE_CHOICE)  # Complaint, Request, or Case
    ticket_state = models.CharField(max_length=128, blank=False, null=True, choices=TICKET_STATE_CHOICE)  # draft,open, in-progress, closed
    ecb_responsible = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    standards = MultiSelectField(max_length=128, blank=True, null=True, choices=STANDARDS_CHOICE)

    program = models.CharField(max_length=1, blank=True, null=True, choices=PROGRAM_CHOICE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, blank=True)
    ep = models.OneToOneField(Ep, on_delete=models.CASCADE, null=True, blank=True)
    filler = models.OneToOneField(Filler, on_delete=models.CASCADE, null=True, blank=True)
    # last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    # flag = models.BooleanField(default=False)

# process

    set_ecb_responsible = models.BooleanField(default=False)
    outcome_reason = models.TextField(blank=True, null=True, help_text="Detailed yet to the point!")

    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_open = models.DateTimeField(blank=True, null=True)
    date_in_progress = models.DateTimeField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)

    # Complaint
    choose_standards = models.BooleanField(default=False)
    contacted_host = models.BooleanField(default=False)
    host_contact_output = models.TextField(blank=True, null=True, help_text="Detailed yet to the point!")
    contacted_ep = models.BooleanField(default=False)
    ep_contact_output = models.TextField(blank=True, null=True, help_text="Detailed yet to the point!")
    complaint_state = models.CharField(max_length=128, blank=True, null=True, choices=COMPLAINT_OUTCOME_CHOICE)

    # Request
    sent_to_icb = models.BooleanField(default=False)
    request_confirmation = models.CharField(max_length=128, blank=True, null=True, choices=REQUEST_OUTCOME_CHOICE)

    # Case
    action_taken = models.TextField(blank=True, null=True, help_text="Detailed yet to the point!")
    icb_escalated = models.BooleanField(default=False)
    oca_file = models.FileField(upload_to=path_and_rename, null=True, blank=True)
    case_result = models.FileField(upload_to=path_and_rename, null=True, blank=True)
    outcome = models.CharField(max_length=128, blank=True, null=True, choices=CASE_OUTCOME_CHOICE)
    amount = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=128, blank=True, null=True, choices=CURRENCY_CHOICE)
    invoice = models.FileField(upload_to=path_and_rename, null=True, blank=True)

# other data

    # complaint
    complaint = models.TextField(blank=True, null=True, help_text="Detailed yet to the point for us to help you best!")
    complaint_type = models.CharField(max_length=128, blank=True, null=True)  # OGX if egypt else = ICX
    complaint_solution = models.TextField(blank=True, null=True)  # solution if complaint is solved
    # image_upload = ImageField(upload_to=None, blank=True, help_text="Kindly add some images if available!")  --STILL NEEDS WORK--

    # Request
    requested_break = models.CharField(max_length=128, blank=True, null=True, choices=STEP_CHOICE)
    request_Reason = models.TextField(blank=True, null=True, help_text="Detailed yet to the point for us to help you best!")

    #case
    case_mail_subject = models.CharField(max_length=128, blank=True, null=True)
    case_brief = models.TextField(blank=True, null=True, help_text="Detailed yet to the point")

    def save(self, *args, **kwargs):

        if self.ecb_responsible is not None:
            self.set_ecb_responsible = True
            self.ticket_state = 'Open'

        # Complaint
        if self.ticket_type == 'Complaint':
            if self.ticket_state == 'Open':
                if self.standards is not None:
                    self.ticket_state = 'In Progress'
            if self.ticket_state == 'In Progress':
                if self.host_contact_output and self.ep_contact_output and self.complaint_state and self.outcome_reason is not None:
                    self.ticket_state = 'Closed'

        # Request
        if self.ticket_type == 'Request':
            if self.ticket_state == 'Open':
                if self.sent_to_icb is True:
                    self.ticket_state = 'In Progress'
            if self.ticket_state == 'In Progress':
                if self.request_confirmation and self.outcome_reason is not None:
                    self.ticket_state = 'Closed'

        # case
        if self.ticket_type == 'Case':
            if self.ticket_state == 'Open':
                if self.action_taken and self.icb_escalated is not None:
                    self.ticket_state = 'In Progress'

            if self.ticket_state == 'In Progress':
                if self.icb_escalated is True:
                    if self.oca_file and self.case_result and self.outcome and self.amount and self.currency and self.invoice and self.outcome_reason is not None:
                        self.ticket_state = 'Closed'
                else:
                    if self.case_result and self.outcome and self.amount and self.currency and self.invoice and self.outcome_reason is not None:
                        self.ticket_state = 'Closed'

        #  setting process dates
        if self.date_open is None and self.ticket_state == 'Open':
            self.date_open = datetime.datetime.now()
        else:
            if self.date_in_progress is None and self.ticket_state == 'In Progress':
                self.date_in_progress = datetime.datetime.now()
            else:
                if self.date_closed is None and self.ticket_state == 'Closed':
                    self.date_closed = datetime.datetime.now()

        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_type




# class Process(models.Model):
#     TICKET_STATE_CHOICE = (('Open', 'Open'), ('In Progress', 'In Progress'),
#                             ('Closed', 'Closed'))
#     COMPLAINT_OUTCOME_CHOICE = (('Solved', 'Solved'), ('Not Solved', 'Not Solved'))
#     REQUEST_OUTCOME_CHOICE = (('Confirmed', 'Confirmed'), ('Not Confirmed', 'Not Confirmed'))
#     CASE_OUTCOME_CHOICE = (('Won', 'Won'), ('Lost', 'Lost'))
#
#     process_state = models.CharField(max_length=128, blank=True, null=True, choices=TICKET_STATE_CHOICE)  # open, in-progress, closed
#     process_type = models.CharField(max_length=128, blank=True, null=True)  # Complaint, Request, or Case
#     set_ecb_responsible = models.BooleanField(default=False)
#     reason = models.TextField(blank=True, null=True, help_text="Detailed yet to the point!")
#
#     # def in_progress_time(self):
#     #
#     #         return None
#     #
#     # in_progress_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False)
#     # # closed_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False)
#
#
#     # Complaint
#     # Open
#     choose_standards = models.BooleanField(default=False)
#     # In Progress
#     contacted_host = models.BooleanField(default=False)
#     host_contact_output = models.TextField(blank=True, null=True, help_text="Detailed yet to the point!")
#     contacted_ep = models.BooleanField(default=False)
#     ep_contact_output = models.TextField(blank=True, null=True, help_text="Detailed yet to the point!")
#     complaint_state = models.CharField(max_length=128, blank=True, null=True, choices=COMPLAINT_OUTCOME_CHOICE)
#     # closed
#
#     # Request
#     # Open
#     # In Progress
#     sent_to_icb = models.BooleanField(default=False)
#     request_state = models.CharField(max_length=128, blank=True, null=True, choices=REQUEST_OUTCOME_CHOICE)
#     # closed
#
#     # Case
#     # Open
#     # In Progress
#     action_taken = models.TextField(blank=True, null=True, help_text="Detailed yet to the point!")
#     icb_escalated = models.BooleanField(default=False)
#     oca_file = models.FileField(upload_to='uploads/process_files/oca')
#     case_result = models.FileField(upload_to='uploads/process_files/case_result')
#     outcome = models.CharField(max_length=128, blank=True, null=True, choices=CASE_OUTCOME_CHOICE)
#     amount = models.IntegerField(blank=True, null=True)
#     currency = models.CharField(max_length=128, blank=True, null=True)
#     invoice = models.FileField(upload_to='uploads/process_files/invoice')
#     # closed
#
#
#
#     def __str__(self):
#         return self.process_type

# class Standard(models.Model):
#     name = models.CharField(max_length=128)
#     number = models.IntegerField()
#
#     def __str__(self):
#         return self.name

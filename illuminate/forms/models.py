from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField


# Population script filled choice models:

class Position(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Offices(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# Main Models

class Filler(models.Model):

    filler_name = models.CharField(max_length=128, blank=True, null=True, help_text="Enter Your Full Name.")
    filler_email = models.EmailField(blank=True, null=True)
    Filler_lc = models.ForeignKey(Offices, null=True, blank=True, on_delete=models.CASCADE)
    filler_position = models.ForeignKey(Position, null=True,blank=True, on_delete=models.CASCADE)
    filler_role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.filler_name


class Ep(models.Model):

    # Required
    ep_name = models.CharField(max_length=128, blank=False, null=False, help_text="Enter Your Full Name.")
    ep_number = models.BigIntegerField(blank=False, null=False, help_text="Enter the number with country code.")
    ep_email = models.EmailField(blank=False, null=False)
    ep_host_lc = models.ForeignKey(Offices, null=True, blank=True, on_delete=models.CASCADE)


    ep_country = CountryField(blank=False, null=True, blank_label='Select home country')
    ep_expa_id = models.IntegerField(blank=False, null=False, help_text="Enter EP ID.")
    opp_id = models.IntegerField(blank=False, null=False, help_text="Enter Opportunity ID.")

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

    # General
    # ticket_id = models.AutoField(primary_key=True, default=1)

    # ticket responsible one to many relationship

    ticket_type = models.CharField(max_length=128, blank=False, null=True)  # complaint or Request
    ticket_state = models.CharField(max_length=128, blank=True, null=True)  # open, in-progress, closed
    comments = models.TextField(blank=True, null=True)
    program = models.CharField(max_length=1, blank=False, null=True, choices=PROGRAM_CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    ep = models.OneToOneField(Ep,on_delete=models.CASCADE,null=True,blank=True)

    # complaint
    complaint = models.TextField(blank=False, null=True, help_text="Detailed yet to the point for us to help you best!")
    complaint_type = models.CharField(max_length=128, blank=False, null=True)  # OGX if egypt else = ICX
    complaint_tag = MultiSelectField(max_length=128, blank=False, null=True, choices=TAG_CHOICE)
    complaint_solution = models.TextField()  # solution if complaint is solved
    # image_upload = ImageField(upload_to=None, blank=True, help_text="Kindly add some images if available!")  --STILL NEEDS WORK--

    # Request
    requested_break = models.CharField(max_length=1, blank=False, null=True, choices=STEP_CHOICE)
    request_Reason = models.TextField(blank=False, null=True,
                                      help_text="Detailed yet to the point for us to help you best!")

    def __str__(self):
        return self.timestamp



# class Complaint(models.Model):
#
#     HOST_LC_CHOICE= request_lcs("1609")
#
#     PROGRAM_CHOICE=(
#         ('GV','Global Volunteer'),
#         ('GE','Global Entrepreneur'),
#         ('GT', 'Global Talent')
#     )
#
#     TAG_CHOICE=(
#         ('Accomodation','Accomodation'),('Job Description','Job Description'),
#         ('Other','Other'),
#     )
#     ep_name = models.CharField(max_length=128, blank=False, null=False, help_text="Enter Your Full Name.")
#     ep_number = models. BigIntegerField(blank=False, null=False, help_text="Enter the number with country code.")
#     ep_email = models.EmailField()
#     ep_country = CountryField(blank=False,null=True, blank_label='Select home country')
#     host_lc = models.CharField(max_length=128, blank=False, null=True, choices=HOST_LC_CHOICE)
#
#     #complaint
#     complaint_id = models.AutoField(primary_key=True)
#     complaint = models.TextField(blank=False, null=False, help_text="Detailed yet to the point for us to help you best!")
#     complaint_tag = MultiSelectField(max_length=128, blank=False, null=True, choices=TAG_CHOICE)
#     program = models.CharField(max_length=128, blank=False, null=True, choices=PROGRAM_CHOICE)
#     #image_upload = ImageField(upload_to=None, blank=True, help_text="Kindly add some images if available!")
#
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#     def __str__(self):
#         return self.email
#

# class Request(models.Model):
#     POSITION_CHOICE = (
#         ('MCP', 'MCP'), ('MCVP', 'MCVP'),
#         ('LCP', 'LCP'), ('LCVP', 'LCVP'),
#         ('Team Leader', 'Team Leader'), ('Coordinator', 'Coordinator'),
#         ('Member', 'Member'),
#     )
#
#     ROLE_CHOICE = (
#         ('IGV', 'IGV'), ('IGE', 'IGE'), ('IGT', 'IGT'),
#         ('OGV', 'OGV'), ('OGE', 'OGE'), ('OGT', 'OGT'),
#         ('F&L', 'F&L'), ('TM', 'TM'), ('Marketing', 'Marketing'),
#     )
#
#     STEP_CHOICE = (
#         ('Approval', 'Approval'),
#         ('Realization', 'Realization'),
#     )
#
#     PROGRAM_CHOICE = (
#         ('GV', 'Global Volunteer'),
#         ('GE', 'Global Entrepreneur'),
#         ('GT', 'Global Talent')
#     )
#     # Request filler info
#     responsible_name = models.CharField(max_length=128, blank=False, null=False, help_text="Enter Your Full Name.")
#     responsible_lc = models.CharField(max_length=1, blank=False, null=True, choices=HOST_LC_CHOICE)
#     responsible_position = models.CharField(max_length=1, blank=False, null=True, choices=POSITION_CHOICE)
#     responsible_role = models.CharField(max_length=1, blank=True, null=True, choices=ROLE_CHOICE)
#
#     # EP info
#     ep_name = models.CharField(max_length=128, blank=False, null=False, help_text="Enter EP's Full Name.")
#     ep_entity = CountryField(blank=False, null=True, blank_label='Select Sending entity')
#     ep_number = models.BigIntegerField(blank=False, null=False, help_text="Enter the number with country code.")
#     ep_email = models.EmailField()
#     ep_id = models.IntegerField(blank=False, null=False, help_text="Enter EP ID.")
#     opp_id = models.IntegerField(blank=False, null=False, help_text="Enter Opportunity ID.")
#
#     # Request
#     request_id = models.AutoField(primary_key=True)
#     requested_break = models.CharField(max_length=1, blank=False, null=True, choices=STEP_CHOICE)
#     program = models.CharField(max_length=1, blank=False, null=True, choices=PROGRAM_CHOICE)
#     request_Reason = models.TextField(blank=False, null=False,
#                                       help_text="Detailed yet to the point for us to help you best!")
#
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#     def __str__(self):
#         return self.email


from django.db import models

# Create your models here.

class Member(models.Model):
    member_last_name = models.CharField('Last Name', max_length=20, null=True, blank=True)
    member_first_name = models.CharField('First Name', max_length=20, null=True, blank=True)
    member_secondary_first_name = models.CharField('Secondary First Name', max_length=20, null=True, blank=True)
    member_child1_name = models.CharField('Child 1 Name', max_length=20, null=True, blank=True)
    member_child2_name = models.CharField('Child 2 Name', max_length=20, null=True, blank=True)
    member_child3_name = models.CharField('Child 3 Name', max_length=20, null=True, blank=True)
    member_child4_name = models.CharField('Child 4 Name', max_length=20, null=True, blank=True)
    member_child5_name = models.CharField('Child 5 Name', max_length=20, null=True, blank=True)
    member_child6_name = models.CharField('Child 6 Name', max_length=20, null=True, blank=True)
    member_child7_name = models.CharField('Child 7 Name', max_length=20, null=True, blank=True)
    member_child8_name = models.CharField('Child 8 Name', max_length=20, null=True, blank=True)
    member_type = models.CharField('Member Type', max_length=20, null=True, blank=True)
    member_duespaid = models.DateField('Dues Paid Date', auto_now=False, auto_now_add=False, null=True, blank=True)
    member_DL = models.CharField('DL', max_length=20, null=True, blank=True)
    member_Volunteer_Interests = models.CharField('Volunteer Interests', max_length=40, null=True, blank=True)
    member_phone = models.CharField('Home Phone', max_length=15, null=True, blank=True)
    member_cell_phone = models.CharField('Cell Phone', max_length=15, null=True, blank=True)
    member_address_street = models.CharField('Street Address', max_length=100, null=True, blank=True)
    member_address_city = models.CharField('City', max_length=50, null=True, blank=True)
    state_choices = (
        ("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),
        ("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),
        ("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),
        ("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),
        ("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),
        ("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),
        ("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),
        ("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),
        ("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),
        ("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),
        ("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),
        ("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),
        ("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),
        ("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming")
    )
    member_address_state = models.CharField('State', max_length=14, choices=state_choices, null=True, blank=True)
    member_address_zip = models.CharField('ZIP Code', max_length=5, null=True, blank=True)
    member_email = models.EmailField('Email', max_length=254, null=True, blank=True)
    member_fax = models.CharField('FAX Number', max_length=15, null=True, blank=True)
    member_notes = models.CharField('Notes', max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.member_first_name} {self.member_last_name}'
from django.db import models

# Create your models here.

class Member(models.Model):
    member_last_name = models.CharField(max_length=20, null=True, blank=True,)
    member_first_name = models.CharField(max_length=20, null=True, blank=True,)
    member_secondary_first_name = models.CharField(max_length=20, null=True, blank=True,)
    member_child1_name = models.CharField(max_length=20, null=True, blank=True,)
    member_child2_name = models.CharField(max_length=20, null=True, blank=True,)
    member_child3_name = models.CharField(max_length=20, null=True, blank=True,)
    member_child4_name = models.CharField(max_length=20, null=True, blank=True,)
    member_child5_name = models.CharField(max_length=20, null=True, blank=True,)
    member_child6_name = models.CharField(max_length=20, null=True, blank=True,)
    member_child7_name = models.CharField(max_length=20, null=True, blank=True,)
    member_child8_name = models.CharField(max_length=20, null=True, blank=True,)
    member_type = models.CharField(max_length=20, null=True, blank=True,)
    member_duespaid = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True,)
    member_DL = models.CharField(max_length=20, null=True, blank=True,)
    member_Volunteer_Interests = models.CharField(max_length=40, null=True, blank=True,)
    member_phone = models.CharField(max_length=15, null=True, blank=True,)
    member_cell_phone = models.CharField(max_length=15, null=True, blank=True,)
    member_address_street = models.CharField(max_length=100, null=True, blank=True,)
    member_address_city = models.CharField(max_length=50, null=True, blank=True,)
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
    member_address_state = models.CharField(max_length=14, choices=state_choices, null=True, blank=True,)
    member_address_zip = models.CharField(max_length=5, null=True, blank=True,)
    member_email = models.CharField(max_length=30, null=True, blank=True,)
    member_fax = models.CharField(max_length=15, null=True, blank=True,)
    member_notes = models.CharField(max_length=100, null=True, blank=True,)

    def __str__(self):
        return f'{self.member_first_name} {self.member_last_name}'
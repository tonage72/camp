from django.db import models

#Create your models here.

class Spot(models.Model):
    spot_identification = models.CharField('Spot ID', max_length=1, null=True, blank=True)
    spot_res_status = models.CharField('Spot Reserve Satus', max_length=1, default='A', blank=False)

    def __str__(self):
        return f'{self.spot_identification}'
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class OrderStadium(models.Model):
    STATUS_CHOICES = (('waiting','waiting'),('accepted','accepted'),('rejected','rejected'))
    match = models.OneToOneField("club.match", verbose_name=_("match"), on_delete=models.CASCADE)
    created_by = models.OneToOneField("club.capitan", verbose_name=_("created by "), on_delete=models.CASCADE)
    status = models.CharField(_("status"),choices=STATUS_CHOICES, max_length=50,default="waiting")
    stadium = models.OneToOneField("club.stadium", verbose_name=_("stadium"), on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
       if self.status == "accepted":
        self.match.stadium=self.stadium
       super(OrderStadium, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return f"{self.match} in {self.stadium} stadium" 
    
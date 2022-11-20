from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Arbitre(models.Model):
    user = models.ForeignKey("account.User", verbose_name=_("user reference"), on_delete=models.CASCADE,related_name="arbitre_user")
    match_number = models.PositiveIntegerField(_("Number of match"),default=0)
    def __str__(self):
        return str(self.user.username)

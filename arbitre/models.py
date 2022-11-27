from django.db import models
from django.utils.translation import gettext_lazy as _


class Arbitre(models.Model):
    user = models.OneToOneField("account.User", verbose_name=_(
        "user reference"), on_delete=models.CASCADE, related_name="arbitre_user")
    match_number = models.PositiveIntegerField(_("Number of match"), default=0)
    available = models.BooleanField(_("available"),default=True)
    def save(self, *args, **kwargs):
       if not self.user.arbitre:
        self.user.arbitre=True
        self.user.save()
       super(Arbitre, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return str(self.user.username)


class OrderArbiterMatchInvite(models.Model):
    capitan = models.ForeignKey("club.capitan", verbose_name=_(
        "capitan"), on_delete=models.CASCADE)
    order = models.ForeignKey("arbitre.OrderArbitreMatch", verbose_name=_(
        "order arbitre"), on_delete=models.CASCADE)
    is_accepted = models.BooleanField(_("accepted"), default=False)
    def save(self, *args, **kwargs):
        if self.is_accepted:
            if OrderArbiterMatchInvite.objects.filter(is_accepted=True).count() > 0:
                self.order.accepted = True
                self.order.status = "accepted"
                self.order.save()
        super(OrderArbiterMatchInvite, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.capitan.user.username

class OrderArbitreMatch(models.Model):
    STATUS=(('accepted','accepted'),('rejected','rejected'),('annuled','annuled'),('waiting','waiting'))
    arbitre = models.ForeignKey("arbitre.arbitre", verbose_name=_(
        "arbitre"), on_delete=models.CASCADE)
    match = models.ForeignKey("club.match", verbose_name=_(
        "match"), on_delete=models.SET_NULL,related_name="order_arbitre_match",null=True)
    price = models.FloatField(_("price"), default=0)
    accepted = models.BooleanField(_("accepted invite"), default=False)
    status = models.CharField(_("Status"), max_length=100,choices=STATUS,default="waiting")
    def save(self, *args, **kwargs):
        """ === create invitation to capitans clubs === """
        if not OrderArbiterMatchInvite.objects.filter(order=self).exists():
            OrderArbiterMatchInvite.objects.create(order=self,capitan=self.match.clube_one.capitan)
            OrderArbiterMatchInvite.objects.create(order=self,capitan=self.match.clube_two.capitan)
        if self.accepted:
            self.match.arbitre = self.arbitre
            self.match.save()
        super(OrderArbitreMatch, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return f"{self.arbitre} match {self.match}"

class MatchCard(models.Model):
    card_choices = (('red','red'),('yellow','yellow'))
    match = models.ForeignKey("club.Match", verbose_name=_("Match"), on_delete=models.CASCADE)
    card = models.CharField(_("Card"), max_length=50,choices=card_choices,null=True)
    player = models.ForeignKey("club.player", verbose_name=_("Player"), on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.card} card to player {self.player.user.username}"
    class Meta:
        unique_together = ('match','card','player')
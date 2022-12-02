from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.
class Capitan(models.Model):
    user = models.OneToOneField("account.User", verbose_name=_("user reference"), on_delete=models.CASCADE,related_name="capitan_user")
    def save(self, *args, **kwargs):
       if not self.user.capitan:
        self.user.capitan=True
        self.user.save()
       super(Capitan, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return str(self.user.username)
class StadiumOwner(models.Model):
    user = models.OneToOneField("account.User", verbose_name=_("user reference"), on_delete=models.CASCADE,related_name="owner")
    stadium_number = models.PositiveIntegerField(_("Number of stadium"),default=0)
    def __str__(self):
        return str(self.user.username)
class Player(models.Model):
    user=models.ForeignKey("account.User", verbose_name=_("user"), on_delete=models.CASCADE,related_name="player")
    nickname = models.CharField(_("Nick Name"), max_length=200)
    def __str__(self):
        return self.user.username



class Clube(models.Model):
    name = models.CharField(_("clube name"), max_length=150)
    capitan = models.OneToOneField("club.Capitan", verbose_name=_("clube leader"), on_delete=models.SET_NULL,null=True)
    active = models.BooleanField(_("Subscription active"),default=False)
    date_created = models.DateTimeField(_("Date Created"), default=timezone.now)
    goals_count = models.PositiveIntegerField(_("Goals number"),default=0)
    match_number = models.PositiveIntegerField(_("Matchs number"),default=0)
    logo = models.ImageField(_("Clube logo"), upload_to="clube_logo",null=True)
    def __str__(self):
        return self.name

class Stadium(models.Model):
    name = models.CharField(_("name"), max_length=100)
    owner = models.ForeignKey("club.StadiumOwner", verbose_name=_("owner of this stad"), on_delete=models.CASCADE)
    localisation = models.CharField(_("localisation"), max_length=100)
    price = models.FloatField(_("price"),default=0)
    promo_price = models.FloatField(_("Promo price"),null=True)
    state=models.CharField(_("state"), max_length=120,null=True)
    image = models.ImageField(_("image"), upload_to="stadium",null=True,blank=True)
    def __str__(self):
        return self.name
class Match(models.Model):
    stadium = models.ForeignKey("club.Stadium", verbose_name=_("stadium"), on_delete=models.SET_NULL,null=True)
    clube_one = models.ForeignKey("club.Clube", verbose_name=_("clube 1"), on_delete=models.SET_NULL,null=True,related_name="clube_number_one")
    clube_two = models.ForeignKey("club.Clube", verbose_name=_("clube 2"), on_delete=models.SET_NULL,null=True,related_name="clube_number_two")
    time_start = models.DateTimeField(_("Time start"),null=True)
    freindly = models.BooleanField(_("freindly match"),default=True)
    score_one = models.PositiveIntegerField(_("Score clube one"),default=0)
    score_two = models.PositiveIntegerField(_("Score clube two"),default=0)
    state = models.CharField(_("State"), max_length=100)
    arbitre = models.ForeignKey("arbitre.Arbitre", verbose_name=_("Arbitre"), on_delete=models.SET_NULL,null=True,blank=True)
    finished = models.BooleanField(_("match finished"),default=False)
    def __str__(self):
        return f"{self.clube_one.name} vs {self.clube_two.name}" if self.clube_one and self.clube_two else str(self.id)

class GoalMatch(models.Model):
    player=models.ForeignKey("club.player", verbose_name=_("player"), on_delete=models.CASCADE)
    is_penalty = models.BooleanField(_("penalty"),default=False)
    match = models.ForeignKey("club.Match", verbose_name=_("match"), on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.player} set goal"
class MatchCard(models.Model):
    CARD_CHOICES = (('red','red'),('yellow','yellow'))
    match = models.ForeignKey("club.match", verbose_name=_(
        "match"), on_delete=models.SET_NULL,related_name="cards_match",null=True)
    card = models.CharField(_("card"),choices=CARD_CHOICES, max_length=50)
    player=models.ForeignKey("club.player", verbose_name=_("player"), on_delete=models.CASCADE,related_name="player_card")
    def __str__(self):
        return f"{self.card} to {self.player.user.username}"


class ClubePlayer(models.Model):
    player=models.ForeignKey("club.player", verbose_name=_("user"), on_delete=models.CASCADE,related_name="player")
    clube = models.ForeignKey("club.Clube", verbose_name=_(""), on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(_("position"),null=True)
    goals = models.PositiveIntegerField(_("Goals number"),default=0)
    def __str__(self):
        return self.player.nickname
class JoinClubeInvite(models.Model):
    clube = models.ForeignKey("club.Clube", verbose_name=_("Clube"), on_delete=models.CASCADE)
    player = models.ForeignKey("club.PLayer", verbose_name=_("player"), on_delete=models.CASCADE,related_name="player_invite")
    accepted = models.BooleanField(_("Accepted invitation"),default=False)
    position = models.PositiveSmallIntegerField(_("position"),null=True)
    def save(self, *args, **kwargs):
       if self.accepted:
        clube_player,clube_player_created=ClubePlayer.objects.get_or_create(player=self.player,clube=self.clube)
        clube_player.position=self.position
        clube_player.save()
       super(JoinClubeInvite, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.player.nickname


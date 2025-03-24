from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Vraboten(models.Model):
    ime_vraboten = models.CharField(max_length=120)
    prezime_vraboten = models.CharField(max_length=120)
    EMBG = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plata = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__ (self):
        return f"{self.ime_vraboten} - {self.prezime_vraboten}"

class Kontakt_Informacii(models.Model):
    ulica = models.CharField(max_length=120)
    br_market = models.IntegerField()
    tel_br = models.IntegerField()
    email = models.EmailField()

    def __str__ (self):
        return f"{self.ulica} - {self.br_market}"

class Proizvod(models.Model):
    ime_proizvod = models.CharField(max_length=120)
    vid_proizvod = [("HR", "HRANA"), ("PI" ,"PIJALOK"), ("PK" ,"PEKARA"), ("KO", "KOZMETIKA"), ("HI", "HIGIENA")]
    vid = models.CharField(max_length=2, choices=vid_proizvod)
    domashen = models.BooleanField()
    kod = models.IntegerField()

    def __str__ (self):
        return f"{self.ime_proizvod}"


class Market(models.Model):
    ime = models.CharField(max_length=100)
    vraboten=models.OneToOneField("Vraboten", on_delete=models.SET_NULL, null=True, blank=True)
    proizvodi = models.ForeignKey(Proizvod, on_delete=models.CASCADE)
    kontakt_informacii = models.ForeignKey(Kontakt_Informacii, on_delete=models.CASCADE)
    broj_na_marketi = models.IntegerField()
    datum_otvaranje = models.DateField()
    korisnik_dodal = models.ForeignKey(User, on_delete=models.CASCADE)
    rabotno_vreme_od = models.DateField()
    rabotno_vreme_do = models.DateField()


    def __str__(self):
        return f"{self.ime}"

class MarketVraboten(models.Model):
    vraboten = models.ForeignKey(Vraboten, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

class MarketProizvod(models.Model):
    proizvod = models.ForeignKey(Proizvod, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    kolicina = models.IntegerField()








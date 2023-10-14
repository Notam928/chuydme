from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ('1', 'Traumatism Oculaire'),
    ('2', 'Infection Oculaire'),
    ('3', 'Maladie Oculaire'),
)


# Create your models here.
class Identification(models.Model):
    numerodossier = models.IntegerField()
    nom = models.CharField(max_length=40, blank=False)
    prenom = models.CharField(max_length=40, blank=False)
    age = models.IntegerField()
    genre= models.CharField(max_length=7,blank=False)
    etatcivil= models.CharField(max_length=40,blank=False)
    profession= models.CharField(max_length=40,blank=False)
    dateconsultation= models.DateField('%m/%d/%Y')
    telephone= models.CharField(max_length=14,blank=False)
    assurer= models.CharField(max_length=3,blank=False)
    assurancesocial= models.CharField(max_length=40,blank=True)
    nomassureur= models.CharField(max_length=40,blank=True)
    domicile= models.CharField(max_length=40,blank=False)
    regionorigine= models.CharField(max_length=20,blank=False)
    statutmalade= models.CharField(max_length=20,blank=False)
    
    def __str__(self):
        return f'{self.nom}-{self.prenom}'
 
class Observation(models.Model):
    motifcon = models.CharField(max_length=255, blank=False)
    poids = models.DecimalField(decimal_places=2,max_digits=9,blank=True,null=True)
    obsnumdoss = models.IntegerField()
    
class Antecedent(models.Model):
    atcdpo = models.TextField(blank=True,null=True)
    atcdfogl = models.CharField(max_length=255)
    atcdnumdoss = models.IntegerField()
    atcddmla = models.CharField(max_length=255)
    atcdaller = models.CharField(max_length=255)
    atcdco = models.CharField(max_length=255)
    atcdce = models.CharField(max_length=255)
    atcdfammedhta = models.CharField(max_length=255)
    atcdfamdiab = models.CharField(max_length=255)
    atcdfamavc = models.CharField(max_length=255)
    comatcdfammed = models.TextField(blank=True,null=True)
    comatcdfammedical = models.TextField(blank=True,null=True)
    fumeur = models.CharField(max_length=255,blank=True,null=True)
    alcool = models.CharField(max_length=255,blank=True,null=True)
    ordinateur = models.CharField(max_length=255,blank=True,null=True)
    fdb = models.CharField(max_length=255,blank=True,null=True)
    lunettes = models.CharField(max_length=255,blank=True,null=True)
    medicaments = models.CharField(max_length=255,blank=True,null=True)
    
    
    
    
class Enquete_System(models.Model):
    es_num_doss = models.IntegerField()
    douleur = models.CharField(max_length=255,blank=True , null =True)
    larme = models.CharField(max_length=255,blank=True , null =True)
    picco = models.CharField(max_length=255,blank=True , null =True)
    prurit = models.CharField(max_length=255,blank=True , null =True)
    grains = models.CharField(max_length=255,blank=True , null =True)
    visuels = models.CharField(max_length=255,blank=True , null =True)
    meta = models.CharField(max_length=255,blank=True , null =True)
    photopsies = models.CharField(max_length=255,blank=True , null =True)
    myodesopsies = models.CharField(max_length=255,blank=True , null =True)
    Cephalees = models.CharField(max_length=255,blank=True , null =True)
    Otalgie = models.CharField(max_length=255,blank=True , null =True)
    acouphene = models.CharField(max_length=255,blank=True , null =True)
    nausees = models.CharField(max_length=255,blank=True , null =True)
    vomissement = models.CharField(max_length=255,blank=True , null =True)
    asthme = models.CharField(max_length=255,blank=True , null =True)
    rhinorrhee = models.CharField(max_length=255,blank=True , null =True)
    autrees = models.CharField(max_length=255,blank=True , null =True)
    


class Exam(models.Model):
    examnumdoss = models.IntegerField()
    inspection = models.CharField(max_length=255,blank=True , null =True)
    reflets = models.CharField(max_length=255,blank=True , null =True)
    cornee = models.CharField(max_length=255,blank=True , null =True)
    corneeod = models.CharField(max_length=255,blank=True , null =True)
    occulomotricite = models.CharField(max_length=255,blank=True , null =True)
    ca = models.CharField(max_length=255,blank=True , null =True)
    caod = models.CharField(max_length=255,blank=True , null =True)
    avog = models.IntegerField(blank=True , null =True)
    avod = models.IntegerField(blank=True , null =True)
    piog = models.DecimalField(decimal_places=2,max_digits=9,blank=True , null =True)
    piod = models.DecimalField(decimal_places=2,max_digits=9,blank=True , null =True)
    sphereog = models.DecimalField(decimal_places=2,max_digits=9,blank=True , null =True)
    cylindreog = models.DecimalField(decimal_places=2,max_digits=9,blank=True , null =True)
    axeog = models.IntegerField(blank=True , null =True)
    sphereod = models.DecimalField(decimal_places=2,max_digits=9,blank=True , null =True)
    cylindreod = models.DecimalField(decimal_places=2,max_digits=9,blank=True , null =True)
    axeod = models.IntegerField(blank=True , null =True)
    cdvaleur = models.DecimalField(decimal_places=2,max_digits=9,blank=True , null =True)
    annexes = models.CharField(max_length=255,blank=True , null =True)
    annexesod = models.CharField(max_length=255,blank=True , null =True)
    iris = models.CharField(max_length=255,blank=True , null =True)
    irisod = models.CharField(max_length=255,blank=True , null =True)
    cristallin = models.CharField(max_length=255,blank=True , null =True)
    cristallinod = models.CharField(max_length=255,blank=True , null =True)
    vitre = models.CharField(max_length=255,blank=True , null =True)
    vitreod = models.CharField(max_length=255,blank=True , null =True)
    retine = models.CharField(max_length=255,blank=True , null =True)
    retineod = models.CharField(max_length=255,blank=True , null =True)
    macula = models.CharField(max_length=255,blank=True , null =True)
    papille = models.CharField(max_length=255,blank=True , null =True)
    exam = models.TextField(blank=True , null =True)
    pupil = models.TextField(blank=True , null =True)
    pupilod = models.TextField(blank=True , null =True)
    nompatient= models.CharField(max_length=255,null =True, editable=False)
    nommedecin = models.CharField(max_length=255,null =True, editable=False)
    
    
    

class Diagnostique(models.Model):
    diagnumdoss = models.IntegerField()
    diagnostiqueog = models.CharField(max_length=255,null=True,blank=True)
    diagnostiqueod = models.CharField(max_length=255,null=True,blank=True)
    commentairediag = models.TextField(max_length=255,null=True,blank=True)
    
    

class Traitement(models.Model):
    traitnumdoss = models.IntegerField()
    traiteencours = models.TextField(null=True,blank=True)
    ccl = models.CharField(max_length=255,null=True,blank=True)
    cat = models.TextField(null=True,blank=True)
    suivi_maladie = models.TextField(max_length=255,null=True,blank=True)
    Tout_rdv = models.TextField(null=True,blank=True)
    duree = models.CharField(max_length=255,null=True,blank=True)
    prescription = models.CharField(max_length=255,null=True,blank=True)
    dose = models.CharField(max_length=255,null=True,blank=True)
    nompatienttr= models.CharField(max_length=255,null =True, editable=False)
    nommedecintr = models.CharField(max_length=255,null =True, editable=False)
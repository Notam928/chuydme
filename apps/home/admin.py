
from django.contrib import admin
from .models import Identification,Observation,Enquete_System,Antecedent,Exam,Diagnostique,Traitement
# Register your models here.
admin.site.register(Identification)
admin.site.register(Observation)
admin.site.register(Enquete_System)
admin.site.register(Antecedent)
admin.site.register(Exam)
admin.site.register(Diagnostique)
admin.site.register(Traitement)

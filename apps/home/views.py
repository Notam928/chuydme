from django import template
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Identification,Observation,Antecedent,Enquete_System,Exam,Diagnostique,Traitement
from django.http import QueryDict
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg,Min,Max

@login_required(login_url="/login/")
def index(request):
    # start_date = request.GET.get('start_date')
    # end_date = request.GET.get('end_date')
                               # Filter data based on the dateconsultation field
    # Identification_list = Identification.objects.filter(dateconsultation__range=[start_date, end_date])
    
    Identification_list = Identification.objects.all() 
    identification_count =Identification_list.count()
    diagnostique_list = Diagnostique.objects.all() 
    exam_list = Exam.objects.all()
    
    from collections import Counter
    
    diagnostic_modalitiesod = Counter(diagnostique.diagnostiqueod for diagnostique in diagnostique_list)
    labelsod = list(diagnostic_modalitiesod.keys())
    frequenciesod = list(diagnostic_modalitiesod.values())
    
    diagnostic_modalitiesog = Counter(diagnostique.diagnostiqueog for diagnostique in diagnostique_list)
    labelsog = list(diagnostic_modalitiesog.keys())
    frequenciesog = list(diagnostic_modalitiesog.values())
    
    professiona = Counter(identification.profession for identification in Identification_list)
    labels_prof = list(professiona.keys())
    
    
    frequencies_prof = list(professiona.values())
    #chambre anterieure
    # camog = Counter(exams.ca for exams in exam_list)
    # labels_caog = list(camog.keys())
    # frequencies_caog = list(camog.values())
    # camod = Counter(exams.caod for exams in exam_list)
    # labels_caod = list(camod.keys())
    # frequencies_caod = list(camod.values())
    
    left_eye_sphere = [float(exams.sphereog) for exams in exam_list]  # Replace with the actual value
    right_eye_sphere = [float(exams.sphereod) for exams in exam_list] 
    left_eye_cylinder = [float(exams.cylindreog) for exams in exam_list] 
    right_eye_cylinder = [float(exams.cylindreod) for exams in exam_list] 
    left_eye_axis = [float(exams.axeog) for exams in exam_list] 
    right_eye_axis = [float(exams.axeod) for exams in exam_list] 
        
     # initialize a null list
   
    
    nombre_Homme = Identification.objects.filter(genre="Homme").count()
    nombre_Femme = Identification.objects.filter(genre="Femme").count()
    age_ranges = [(0, 10), (11, 20), (21, 30), (31, 40),(41,50),(51,60),(61,70),(71,80),(81,90),(91,100)]  # Définissez vos tranches d'âge
    age_counts = []

    for age_range in age_ranges:
        min_age, max_age = age_range
        count = Identification.objects.filter(age__gte=min_age, age__lte=max_age).count()
        age_counts.append(count)
        
    nombre_hommes = Identification.objects.filter(genre="Homme", statutmalade='Nouveau Malade').count()
    nombre_femmes = Identification.objects.filter(genre="Femme", statutmalade='Nouveau Malade').count()
    
    if identification_count==0:
        identification_count = 0.001
        propor_homme = (nombre_Homme/identification_count)*100
        propor_femme = (nombre_Femme/identification_count)*100
        propor_homme_nc = (nombre_hommes/identification_count)*100
        propor_femme_nc = (nombre_femmes/identification_count)*100
    else:
        propor_homme = round((nombre_Homme/identification_count)*100,2)
        propor_femme = round((nombre_Femme/identification_count)*100,2)
        propor_homme_nc = round((nombre_hommes/identification_count)*100,2)
        propor_femme_nc = round((nombre_femmes/identification_count)*100,2)
        
    total_suivi = Traitement.objects.filter(suivi_maladie='Oui').count()
    total_evo = Traitement.objects.filter(ccl='Evolution Favorable').count()
    total_diag= Diagnostique.objects.all().count()
    average_age_man_dict = Identification.objects.filter(genre='Homme').aggregate(Avg('age'))
    average_age_man = round(average_age_man_dict["age__avg"],2)
    average_age_woman_dict = Identification.objects.filter(genre='Femme').aggregate(Avg('age'))
    average_age_woman = round(average_age_woman_dict["age__avg"],2)
    
    atcd_avc = Antecedent.objects.filter(atcdfamavc='Presence AVC').count()
    atcd_diab = Antecedent.objects.filter(atcdfamdiab='Presence Diabete').count()
    atcd_hta = Antecedent.objects.filter(atcdfammedhta='HTA Present').count()
    aco = Enquete_System.objects.filter(acouphene='Acouphene Presente').count()
    otal = Enquete_System.objects.filter(Otalgie='Otalgie Presente').count()
    sens = Enquete_System.objects.filter(grains='Sensation Grains Presente').count()
    vis = Enquete_System.objects.filter(visuels='Flou Visuel Presente').count()
    aller = Antecedent.objects.filter(atcdaller='Allergie Presente').count()
    glau = Antecedent.objects.filter(atcdfogl='Glaucome Presente').count()
    cecite = Antecedent.objects.filter(atcdce='Cecite Presente').count()
    co = Antecedent.objects.filter(atcdco='deja effectuer').count()
   
   
   
    nouveau_malade_homme = Identification.objects.filter(genre='Homme',statutmalade= 'Nouveau Malade').count()
    nouveau_malade_femme = Identification.objects.filter(genre='Femme',statutmalade= 'Nouveau Malade').count()
    ancien_malade_homme = Identification.objects.filter(genre='Homme',statutmalade= 'Ancien Malade').count()
    ancien_malade_femme = Identification.objects.filter(genre='Femme',statutmalade= 'Ancien Malade').count()
    
    
    
    tyndall0og = Exam.objects.filter(ca= 'Tyndall 0').count()
    tyndall0_1og = Exam.objects.filter(ca= 'Tyndall 0-1+').count()
    tyndall1og = Exam.objects.filter(ca= 'Tyndall 1+').count()
    tyndall2og = Exam.objects.filter(ca= 'Tyndall 2+').count()
    tyndall3og = Exam.objects.filter(ca= 'Tyndall 3+').count()
    tyndall4og = Exam.objects.filter(ca= 'Tyndall 4+').count()
    
    
    tyndall0od = Exam.objects.filter(caod= 'Tyndall 0').count()
    tyndall0_1od = Exam.objects.filter(caod= 'Tyndall 0-1+').count()
    tyndall1od = Exam.objects.filter(caod= 'Tyndall 1+').count()
    tyndall2od = Exam.objects.filter(caod= 'Tyndall 2+').count()
    tyndall3od = Exam.objects.filter(caod= 'Tyndall 3+').count()
    tyndall4od = Exam.objects.filter(caod= 'Tyndall 4+').count()
   
    
    
    
    #Acuite Visuel
    
    Acuite_visual_data_od = Exam.objects.all().aggregate(
        min_visual_acuity=Min('avod'),
        max_visual_acuity=Max('avod'),
        avg_visual_acuity=Avg('avod')
    )
    Acuite_visual_data_og = Exam.objects.all().aggregate(
        min_visual_acuity=Min('avog'),
        max_visual_acuity=Max('avog'),
        avg_visual_acuity=Avg('avog')
    )
    
    PIO_od = Exam.objects.all().aggregate(
        min_pio=Min('piod'),
        max_pio=Max('piod'),
        avg_pio=Avg('piod')
    )
    PIO_og = Exam.objects.all().aggregate(
        min_pio=Min('piog'),
        max_pio=Max('piog'),
        avg_pio=Avg('piog')
    )
    
    Age =Identification.objects.all().aggregate(
        min_=Min('age'),
        max_=Max('age'),
    )

    
    context = {'segment': 'index','nouveau_malade_homme':nouveau_malade_homme,'aller':aller,'glau':glau,'cecite':cecite,'co':co,
               'labels_prof':labels_prof,'frequencies_prof':frequencies_prof,"Age":Age,'propor_homme_nc':propor_homme_nc,'propor_femme_nc':propor_femme_nc,
               'Acuite_visual_data_od': Acuite_visual_data_od,'Acuite_visual_data_og': Acuite_visual_data_og,'PIO_og':PIO_og,'PIO_od':PIO_od, 'left_eye_sphere': left_eye_sphere,
                'right_eye_sphere': right_eye_sphere,
                'left_eye_cylinder': left_eye_cylinder,
                'right_eye_cylinder': right_eye_cylinder,
                'left_eye_axis': left_eye_axis,
                'right_eye_axis': right_eye_axis,
                'tyndall0og':tyndall0og,
                'tyndall0-1og':tyndall0_1og,
                'tyndall2og':tyndall2og,
                'tyndall3og':tyndall3og,
                'tyndall4og':tyndall4og,
                'tyndall0od':tyndall0od,
                'tyndall0-1od':tyndall0_1od,
                'tyndall2od':tyndall2od,
                'tyndall3od':tyndall3od,
                'tyndall4od':tyndall4od,
               'nouveau_malade_femme':nouveau_malade_femme,'ancien_malade_homme':ancien_malade_homme,'ancien_malade_femme':ancien_malade_femme,'aco':aco,'otal':otal,'sens':sens,'vis':vis,'atcd_hta':atcd_hta,'atcd_avc':atcd_avc,'atcd_diab':atcd_diab,'age_counts': age_counts, 'age_ranges': age_ranges,'labelsod': labelsod,'frequenciesod':frequenciesod,'labelsog': labelsog,'frequenciesog':frequenciesog,'identification_count':identification_count,'total_suivi':total_suivi,'total_diag':total_diag,'total_evo':total_evo,'average_age_man':average_age_man,'average_age_woman':average_age_woman,'propor_homme':propor_homme,'propor_femme':propor_femme}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required
def createidentification(request):
    if request.method == 'POST':
        numerodossier=request.POST.get('numerodossier')
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        age=request.POST.get('age')
        genre=request.POST.get('genre')
        etatcivil=request.POST.get('etatcivil')
        profession=request.POST.get('profession')
        dateconsultation=request.POST.get('dateconsultation')
        telephone=request.POST.get('telephone')
        assurer=request.POST.get('assurer')
        assurancesocial=request.POST.get('assurancesocial')
        nomassureur=request.POST.get('nomassureur')
        domicile=request.POST.get('domicile')
        regionorigine=request.POST.get('regionorigine')
        statutmalade=request.POST.get('statutmalade')
        check_existing =Identification.objects.filter(numerodossier=numerodossier).exists()
    
        if check_existing:
            messages.error(request, 'Le numero de dossier existe deja!')
            return redirect('/createidentification')
        elif not numerodossier.isdigit():
            messages.error(request, "Entrez le numero de dossier !")
            return redirect('/createidentification')
        elif nom == "":
            messages.error(request, "Entrez le nom !")
            return redirect('/createidentification')
        elif prenom == "":
            messages.error(request, "Entrez le prenom !")
            return redirect('/createidentification')
        elif genre == "":
            messages.error(request, "Entrez le genre !")
            return redirect('/createidentification')
        elif etatcivil == "":
            messages.error(request, "Entrez l'etat civil !")
            return redirect('/createidentification')
        elif profession == "":
            messages.error(request, "Entrez la profession !")
            return redirect('/createidentification')
        elif domicile == "":
            messages.error(request, "Entrez le domicile !")
            return redirect('/createidentification')
        elif not age.isdigit():
            messages.error(request, "Entrez un nombre entier comme l'age!")
            return redirect('/createidentification')
        elif dateconsultation == "":
            messages.error(request, "Entrez La date de consultation!")
            return redirect('/createidentification')
        else:
            query = Identification(numerodossier=numerodossier,nom=nom,prenom=prenom,age=age,genre=genre,etatcivil=etatcivil,profession=profession,
                               dateconsultation=dateconsultation,telephone=telephone,assurer=assurer,assurancesocial=assurancesocial,nomassureur=nomassureur,
                               domicile=domicile,regionorigine=regionorigine,statutmalade=statutmalade)
            query.save()
            messages.success(request, 'Les Identifications ont été enregistrés avec succès!')
            return redirect('/listidentification')
    else: 
        return render(request, 'home/saveidentification.html')


@login_required(login_url="/login/")
def listidentification(request):
    Identification_list = Identification.objects.all()
    paginator = Paginator(Identification_list,100000000000)
    page = request.GET.get('page')
    try:
        identifications = paginator.page(page)
    except PageNotAnInteger:
        identifications = paginator.page(1)
    except EmptyPage:
        identifications = paginator.page(paginator.num_pages)
    return render(request, 'home/listidentification.html', {'identifications': identifications})


@login_required(login_url="/login/")
def editidentification(request, id):
    identification = Identification.objects.get(id=id)
    context = {'identification': identification}
    return render(request, 'home/editidentification.html', context)


@login_required(login_url="/login/")
def updateidentification(request, id):
    if request.method == 'POST':
        numerodossier=request.POST['numerodossier']
        nom=request.POST['nom']
        prenom=request.POST['prenom']
        age= request.POST['age']
        genre=request.POST['genre']
        etatcivil=request.POST['etatcivil']
        profession=request.POST['profession']
        dateconsultation=request.POST['dateconsultation']
        telephone=request.POST['telephone']
        assurer=request.POST['assurer']
        assurancesocial=request.POST['assurancesocial']
        nomassureur=request.POST['nomassureur']
        domicile=request.POST['domicile']
        regionorigine=request.POST['regionorigine']
        statutmalade=request.POST['statutmalade']
        identification = Identification.objects.get(id=id)
        identification.numerodossier=numerodossier
        identification.nom=nom
        identification.prenom=prenom
        identification.age= age
        identification.genre=genre
        identification.etatcivil=etatcivil
        identification.profession=profession
        identification.dateconsultation=dateconsultation
        identification.telephone=telephone
        identification.assurer=assurer
        identification.assurancesocial=assurancesocial
        identification.nomassureur=nomassureur
        identification.domicile=domicile
        identification.regionorigine=regionorigine
        identification.statutmalade=statutmalade
        identification.save()
        messages.success(request, 'Les Identifications ont été mises à jours avec succès!')
        return redirect('/listidentification')
    iden = Identification.objects.get(id=id)
    context = {"iden":iden}
    return render(request,'home/editidentification.html',context)

@login_required(login_url="/login/")
def deleteidentification(request,id):
    obj = get_object_or_404(Identification, id=id)
    obj.delete()
    return redirect('/listidentification')

@login_required(login_url="/login/")
def createobservation(request):
    if request.method == 'POST':
        motifcon=request.POST.get('motifcon')
        poids=request.POST.get('poids')
        obsnumdoss=request.POST.get('obsnumdoss')
        check_existing =Observation.objects.filter(obsnumdoss=obsnumdoss).exists()
        if check_existing:
            messages.error(request, 'Le numero de dossier existe deja!')
            return redirect('/createobservation')
        elif motifcon == "":
            messages.error(request, "Entrez le motif de consultation !")
            return redirect('/createobservation')
        else:
            query = Observation(motifcon=motifcon,poids=poids,obsnumdoss=obsnumdoss)
            query.save()
            messages.success(request, 'Les Observations ont été enregistrés avec succès!')
            return redirect('/listobservation')
    else:
        return render(request, 'home/saveobservation.html')


# def createobservation(request):
#     form = ObservationForm()
#     if request.method == 'POST':
#         form = ObservationForm(request.POST)
#         if form.is_valid():
#             motifcon = form.cleaned_data['motifcon']
#             plaintes = form.cleaned_data['plaintes']
#             poids = form.cleaned_data['poids']
#             identification = form.cleaned_data['identification']
#             Observation.objects.create(
#                 motifcon=motifcon,
#                 plaintes=plaintes,
#                 poids=poids,
#                 identification=identification,
#             )
#             return redirect('/listobservation')
#     context = {
#         'form': form
#     }
#     return render(request, 'home/saveobservation.html', context)
     
@login_required(login_url="/login/")
def listobservation(request):
    Observation_list = Observation.objects.all()
    paginator = Paginator(Observation_list,100000000000)
    page = request.GET.get('page')
    try:
        observations = paginator.page(page)
    except PageNotAnInteger:
        observations = paginator.page(1)
    except EmptyPage:
        observations = paginator.page(paginator.num_pages)
    return render(request, 'home/listobservation.html', {'observations': observations})


@login_required(login_url="/login/")
def editobservation(request, id):
    observation = Observation.objects.get(id=id)
    context = {'observation': observation}
    return render(request, 'home/editobservation.html', context)


@login_required(login_url="/login/")
def updateobservation(request, id):
    if request.method == 'POST':
        motifcon=request.POST['motifcon']
        poids=request.POST['poids']
        obsnumdoss= request.POST['obsnumdoss']
        observation = Observation.objects.get(id=id)
        observation.motifcon=motifcon
        observation.poids=poids
        observation.obsnumdoss=obsnumdoss
        observation.save()
        messages.success(request, 'Les Observations ont été mises à jours avec succès!')
        return redirect('/listobservation')
    obser = Observation.objects.get(id=id)
    context = {"obser":obser}
    return render(request,'home/editobservation.html',context)


# def updateobservation(request, id):
#     item = Observation.objects.get(id=id)
#     if request.method == 'POST':
#         form = ObservationForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('/listobservation')
#     else:
#         form = ObservationForm(instance=item)
#     context = {
#         'form': form,
#     }
#     return render(request, 'home/editobservation.html', context)


@login_required(login_url="/login/")
def deleteobservation(request,id):
    obj = get_object_or_404(Observation, id=id)
    obj.delete()
    return redirect('/listobservation')




# @login_required(login_url="/login/")
# def listatcd(request):
#     atcd_list = Antecedent.objects.all()
#     paginator = Paginator(atcd_list,100000000000)
#     page = request.GET.get('page')
#     try:
#         atcds = paginator.page(page)
#     except PageNotAnInteger:
#         atcds = paginator.page(1)
#     except EmptyPage:
#         atcds = paginator.page(paginator.num_pages)
#     return render(request, 'home/listatcd.html', {'atcds': atcds})

# @login_required(login_url="/login/")
# def createatcd(request):
#     formatcd = AntecedentForm(request.POST)
#     if request.method == 'POST':
#         formatcd = AntecedentForm(request.POST)
#         if formatcd.is_valid():
#             atcdpo = formatcd.cleaned_data['atcdpo']
#             idenatcd = formatcd.cleaned_data['idenatcd']
#             Antecedent.objects.create(
#                 atcdpo=atcdpo,
#                 idenatcd=idenatcd,
#             ) 
#             return redirect('/listatcd')
#     context = {
#         'form': formatcd
#     }
#     return render(request, 'home/saveatcd.html', context)

@login_required(login_url="/login/")
def createatcd(request):
    if request.method == 'POST':
        atcdpolist=request.POST.getlist('atcdpo')
        atcdpo = ', '.join(atcdpolist)
        atcdnumdoss=request.POST.get('atcdnumdoss')
        atcdfogl=request.POST.get('atcdfogl')
        atcddmla=request.POST.get('atcddmla')
        atcdaller=request.POST.get('atcdaller')
        atcdco=request.POST.get('atcdco')
        atcdce=request.POST.get('atcdce')
        atcdfammedhta=request.POST.get('atcdfammedhta')
        atcdfamdiab=request.POST.get('atcdfamdiab')
        atcdfamavc=request.POST.get('atcdfamavc')
        comatcdfammed=request.POST.get('comatcdfammed')
        comatcdfammedical=request.POST.get('comatcdfammedical')
        fumeur=request.POST.get('fumeur')
        alcool=request.POST.get('alcool')
        ordinateur=request.POST.get('ordinateur')
        fdb=request.POST.get('fdb')
        lunettes=request.POST.get('lunettes')
        medicaments=request.POST.get('medicaments')

        check_existing =Antecedent.objects.filter(atcdnumdoss=atcdnumdoss).exists()
    
        if check_existing:
            messages.error(request, 'Le numero de dossier existe deja!')
            return redirect('/createantecedent')
        elif atcdfogl == "":
            messages.error(request, "Choissisez GLAUCOME presente ou absente !")
            return redirect('/createantecedent')
        elif atcddmla == "":
            messages.error(request, "Choissisez si DMLA presente ou absente !")
            return redirect('/createantecedent')
        elif atcdaller == "":
            messages.error(request, "Choissisez si Allergie presente ou absente !")
            return redirect('/createantecedent')
        elif atcdco == "":
            messages.error(request, "Choissisez si Chirugie Oculaire presente ou absente !")
            return redirect('/createantecedent')
        elif atcdce == "":
            messages.error(request, "Choissisez si Cecite presente ou absente !")
            return redirect('/createantecedent')
        elif atcdfammedhta == "":
            messages.error(request, "Choissisez si HTA presente ou absente !")
            return redirect('/createantecedent')
        elif atcdfamdiab == "":
            messages.error(request, "Choissisez si Diabete presente ou absente !")
            return redirect('/createantecedent')
        elif atcdfamavc == "":
            messages.error(request, "Choissisez si AVC presente ou absente !")
            return redirect('/createantecedent')
        else:
            query = Antecedent(atcdpo=atcdpo,fumeur=fumeur,alcool=alcool,ordinateur=ordinateur,fdb=fdb,lunettes=lunettes,medicaments=medicaments,atcdnumdoss=atcdnumdoss,atcdfogl=atcdfogl,atcddmla=atcddmla,atcdaller=atcdaller,atcdco=atcdco,atcdce=atcdce,atcdfammedhta=atcdfammedhta,atcdfamdiab=atcdfamdiab,atcdfamavc=atcdfamavc,comatcdfammed=comatcdfammed,comatcdfammedical=comatcdfammedical)
            query.save()
            messages.success(request, 'Les Antécédents ont été enregistrés avec succès!')
            return redirect('/listatcd')
    else:
        return render(request, 'home/saveatcd.html')
    

@login_required(login_url="/login/")
def listatcd(request):
    atcd_list = Antecedent.objects.all()
    paginator = Paginator(atcd_list,100000000000)
    page = request.GET.get('page')
    try:
        atcds = paginator.page(page)
    except PageNotAnInteger:
        atcds = paginator.page(1)
    except EmptyPage:
        atcds = paginator.page(paginator.num_pages)
    return render(request, 'home/listatcd.html', {'atcds': atcds})

@login_required(login_url="/login/")
def editatcd(request, id):
    antecedent = Antecedent.objects.get(id=id)
    context = {'antecedent': antecedent}
    return render(request, 'home/editatcd.html', context)


@login_required(login_url="/login/")
def updateatcd(request, id):
    if request.method == 'POST':
        atcdpolist=request.POST.getlist('atcdpo')
        atcdpo = ', '.join(atcdpolist)
        atcdnumdoss=request.POST['atcdnumdoss']
        atcdfogl=request.POST.get('atcdfogl')
        atcddmla=request.POST.get('atcddmla')
        atcdaller=request.POST.get('atcdaller')
        atcdco=request.POST.get('atcdco')
        atcdce=request.POST.get('atcdce')
        atcdfammedhta=request.POST.get('atcdfammedhta')
        atcdfamdiab=request.POST.get('atcdfamdiab')
        atcdfamavc=request.POST.get('atcdfamavc')
        comatcdfammed=request.POST.get('comatcdfammed')
        comatcdfammedical=request.POST.get('comatcdfammedical')
        fumeur=request.POST.get('fumeur')
        alcool=request.POST.get('alcool')
        ordinateur=request.POST.get('ordinateur')
        fdb=request.POST.get('fdb')
        lunettes=request.POST.get('lunettes')
        medicaments=request.POST.get('medicaments')
        
        antecedent = Antecedent.objects.get(id=id)
        antecedent.atcdpo=atcdpo
      
        antecedent.atcdfogl=atcdfogl
        antecedent.atcddmla=atcddmla
        antecedent.atcdaller=atcdaller
        antecedent.atcdco=atcdco
        antecedent.atcdce=atcdce
        antecedent.atcdfammedhta=atcdfammedhta
        antecedent.atcdfamdiab=atcdfamdiab
        antecedent.atcdfamavc=atcdfamavc
        antecedent.comatcdfammed=comatcdfammed
        antecedent.comatcdfammedical=comatcdfammedical
        antecedent.fumeur=fumeur
        antecedent.alcool=alcool
        antecedent.ordinateur=ordinateur
        antecedent.fdb=fdb
        antecedent.lunettes=lunettes
        antecedent.medicaments=medicaments
      
        antecedent.atcdnumdoss=atcdnumdoss
        antecedent.save()
        messages.success(request, 'Les Antécédents ont été mises à jours avec succès !')
        return redirect('/listatcd')
    ante = Antecedent.objects.get(id=id)
    context = {"ante":ante}
    return render(request,'home/editatcd.html',context)


@login_required(login_url="/login/")
def deleteatcd(request,id):
    obj = get_object_or_404(Antecedent, id=id)
    obj.delete()
    return redirect('/listatcd')


@login_required(login_url="/login/")
def createenquetesystem(request):
    if request.method == 'POST':
        es_num_doss=request.POST.get('es_num_doss')
        douleur=request.POST.get('douleur')
        larme=request.POST.get('larme')
        picco=request.POST.get('picco')
        prurit=request.POST.get('prurit')
        grains=request.POST.get('grains')
        visuels=request.POST.get('visuels')
        meta=request.POST.get('meta')
        photopsies=request.POST.get('photopsies')
        myodesopsies=request.POST.get('myodesopsies')
        Cephalees=request.POST.get('Cephalees')
        Otalgie=request.POST.get('Otalgie')
        acouphene=request.POST.get('acouphene')
        nausees=request.POST.get('nausees')
        vomissement=request.POST.get('vomissement')
        asthme=request.POST.get('asthme')
        rhinorrhee=request.POST.get('rhinorrhee')
        autrees=request.POST.get('autrees')
        check_existing =Enquete_System.objects.filter(es_num_doss=es_num_doss).exists()
        if check_existing:
            messages.error(request, 'Le numero de dossier existe deja!')
            return redirect('/createenquetesystem')
        else:
            query = Enquete_System(asthme=asthme,rhinorrhee=rhinorrhee,autrees=autrees,es_num_doss=es_num_doss,douleur=douleur,larme=larme,picco=picco,prurit=prurit,grains=grains,visuels=visuels,meta=meta,photopsies=photopsies,myodesopsies=myodesopsies,Cephalees=Cephalees,Otalgie=Otalgie,acouphene=acouphene,nausees=nausees,vomissement=vomissement)
            query.save()
            messages.success(request, 'Les Enquêtes de Systeme ont été enregistrés avec succès!')
            return redirect('/listenquetesysteme')
    else:
        return render(request, 'home/saveenquetesysteme.html')
    
    

@login_required(login_url="/login/")
def listenquetesysteme(request):
    enquetes_list = Enquete_System.objects.all()
    paginator = Paginator(enquetes_list,100000000000)
    page = request.GET.get('page')
    try:
        enquetes = paginator.page(page)
    except PageNotAnInteger:
        enquetes = paginator.page(1)
    except EmptyPage:
        enquetes = paginator.page(paginator.num_pages)
    return render(request, 'home/listenquetesysteme.html', {'enquetes': enquetes})


@login_required(login_url="/login/")
def editenquetes(request, id):
    enquete = Enquete_System.objects.get(id=id)
    context = {'enquete': enquete}
    return render(request, 'home/editenquetesysteme.html', context)



@login_required(login_url="/login/")
def updateenquetes(request, id):
    if request.method == 'POST':
        es_num_doss=request.POST.get('es_num_doss')
        douleur=request.POST.get('douleur')
        larme=request.POST.get('larme')
        picco=request.POST.get('picco')
        prurit=request.POST.get('prurit')
        grains=request.POST.get('grains')
        visuels=request.POST.get('visuels')
        meta=request.POST.get('meta')
        photopsies=request.POST.get('photopsies')
        myodesopsies=request.POST.get('myodesopsies')
        Cephalees=request.POST.get('Cephalees')
        Otalgie=request.POST.get('Otalgie')
        acouphene=request.POST.get('acouphene')
        nausees=request.POST.get('nausees')
        vomissement=request.POST.get('vomissement')
        asthme=request.POST.get('asthme')
        rhinorrhee=request.POST.get('rhinorrhee')
        autrees=request.POST.get('autrees')
        enquete = Enquete_System.objects.get(id=id)
        enquete.es_num_doss = es_num_doss
        enquete.douleur = douleur
        enquete.larme = larme
        enquete.picco = picco
        enquete.prurit = prurit
        enquete.grains = grains
        enquete.visuels = visuels
        enquete.meta = meta
        enquete.photopsies = photopsies
        enquete.myodesopsies = myodesopsies
        enquete.Cephalees = Cephalees
        enquete.Otalgie = Otalgie
        enquete.acouphene = acouphene
        enquete.nausees = nausees
        enquete.vomissement = vomissement
        enquete.asthme = asthme
        enquete.rhinorrhee = rhinorrhee
        enquete.autrees = autrees
        enquete.save()
        messages.success(request, 'Les Enquêtes de systeme ont été mises à jours avec succès!')
        return redirect('/listenquetesysteme')
    enqu = Enquete_System.objects.get(id=id)
    context = {"enqu":enqu}
    return render(request,'home/editenquetesysteme.html',context)


@login_required(login_url="/login/")
def deleteenquetes(request,id):
    obj = get_object_or_404(Enquete_System, id=id)
    obj.delete()
    return redirect('/listenquetesysteme')



@login_required(login_url="/login/")
def createexam(request):
    if request.method == 'POST':
        examnumdoss=request.POST.get('examnumdoss')
        inspection=request.POST.get('inspection')
        occulomotricite=request.POST.get('occulomotricite')
        avog=request.POST.get('avog')
        avod=request.POST.get('avod')
        piod=request.POST.get('piod')
        piog=request.POST.get('piog')
        sphereog=request.POST.get('sphereog')
        cylindreog=request.POST.get('cylindreog')
        axeog=request.POST.get('axeog')
        sphereod=request.POST.get('sphereod')
        cylindreod=request.POST.get('cylindreod')
        axeod=request.POST.get('axeod')
        cdvaleur=request.POST.get('cdvaleur')
        annexes=request.POST.get('annexes')
        annexesod=request.POST.get('annexesod')
        iris=request.POST.get('iris')
        irisod=request.POST.get('irisod')
        cristallin=request.POST.get('cristallin')
        cristallinod=request.POST.get('cristallinod')
        vitre=request.POST.get('vitre')
        vitreod=request.POST.get('vitreod')
        retine=request.POST.get('retine')
        retineod=request.POST.get('retineod')
        macula=request.POST.get('macula')
        papille=request.POST.get('papille')
        pupillist=request.POST.getlist('pupil')
        pupil = ', '.join(pupillist)
        pupilodlist=request.POST.getlist('pupilod')
        pupilod = ', '.join(pupilodlist)
        ca=request.POST.get('ca')
        caod=request.POST.get('caod')
        cornee=request.POST.get('cornee')
        corneeod=request.POST.get('corneeod')
        examlist=request.POST.getlist('exam')
        exam = ', '.join(examlist)
        reflets=request.POST.get('reflets')
        
         # Create a copy of the request.POST QueryDict
        modified_data = QueryDict(request.POST.urlencode(), mutable=True)
        nompatient = modified_data.pop('nompatient', None)
        modified_data._mutable = False
        modified_data1 = QueryDict(request.POST.urlencode(), mutable=True)
        nommedecin = modified_data1.pop('nommedecin', None)
        modified_data1._mutable = False
        check_existing =Exam.objects.filter(examnumdoss=examnumdoss).exists()
        if check_existing:
            messages.error(request, 'Le numero de dossier existe deja!')
            return redirect('/createexam')
        else:
            query = Exam(annexesod=annexesod,vitreod=vitreod,retineod=retineod,pupilod=pupilod,caod=caod,corneeod=corneeod,examnumdoss=examnumdoss,inspection=inspection,irisod=irisod,cristallinod=cristallinod,occulomotricite=occulomotricite,avog=avog,avod=avod,piod=piod,piog=piog,sphereog=sphereog,cylindreog=cylindreog,axeog=axeog,sphereod=sphereod,cylindreod=cylindreod,axeod=axeod,cdvaleur=cdvaleur,annexes=annexes,cornee=cornee,iris=iris,cristallin=cristallin,vitre=vitre,retine=retine,macula=macula,papille=papille,pupil=pupil,ca=ca,exam=exam,reflets=reflets)
            query.save()
            messages.success(request, 'Les Examens ont été enregistrés avec succès!')
            return redirect('/listexam')
        
       
    else:
        return render(request, 'home/saveexam.html')
    
    
    
    
@login_required(login_url="/login/")
def listexam(request):
    exams_list = Exam.objects.all()
    paginator = Paginator(exams_list,100000000000)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)
    return render(request, 'home/listexam.html', {'exams': exams})


@login_required(login_url="/login/")
def editexam(request, id):
    exam = Exam.objects.get(id=id)
    context = {'exam': exam}
    return render(request, 'home/editexam.html', context)


@login_required(login_url="/login/")
def updateexam(request, id):
    if request.method == 'POST':
        examnumdoss=request.POST.get('examnumdoss')
        inspection=request.POST.get('inspection')
        occulomotricite=request.POST.get('occulomotricite')
        avog=request.POST.get('avog')
        avod=request.POST.get('avod')
        piod=request.POST.get('piod')
        piog=request.POST.get('piog')
        sphereog=request.POST.get('sphereog')
        cylindreog=request.POST.get('cylindreog')
        axeog=request.POST.get('axeog')
        sphereod=request.POST.get('sphereod')
        cylindreod=request.POST.get('cylindreod')
        axeod=request.POST.get('axeod')
        cdvaleur=request.POST.get('cdvaleur')
        annexes=request.POST.get('annexes')
        annexesod=request.POST.get('annexes')
        iris=request.POST.get('iris')
        irisod=request.POST.get('iris')
        cristallin=request.POST.get('cristallin')
        cristallinod=request.POST.get('cristallin')
        vitre=request.POST.get('vitre')
        vitreod=request.POST.get('vitre')
        retine=request.POST.get('retine')
        retineod=request.POST.get('retine')
        macula=request.POST.get('macula')
        papille=request.POST.get('papille')
        pupillist=request.POST.getlist('pupil')
        pupil = ', '.join(pupillist)
        pupilodlist=request.POST.getlist('pupilod')
        pupilod = ', '.join(pupilodlist)
        ca=request.POST.get('ca')
        caod=request.POST.get('caod')
        cornee=request.POST.get('cornee')
        corneeod=request.POST.get('corneeod')
        examlist=request.POST.getlist('exam')
        exam = ', '.join(examlist)
        reflets=request.POST.get('reflets')
        exam_ = Exam.objects.get(id=id)
        exam_.examnumdoss = examnumdoss
        exam_.inspection = inspection
        exam_.reflets = reflets
        exam_.occulomotricite = occulomotricite
        exam_.avod = avod
        exam_.avog = avog
        exam_.piog = piog
        exam_.piod = piod
        exam_.sphereog = sphereog
        exam_.cylindreog = cylindreog
        exam_.axeog = axeog
        exam_.sphereod = sphereod
        exam_.cylindreod = cylindreod
        exam_.axeod = axeod
        exam_.cdvaleur = cdvaleur
        exam_.annexes = annexes
        exam_.annexesod = annexesod
        exam_.cornee = cornee
        exam_.corneeod = corneeod
        exam_.iris = iris
        exam_.irisod = irisod
        exam_.cristallin = cristallin
        exam_.cristallinod = cristallinod
        exam_.vitre = vitre
        exam_.vitreod = vitreod
        exam_.retine = retine
        exam_.retineod = retineod
        exam_.macula = macula
        exam_.papille = papille
        exam_.pupil = pupil 
        exam_.pupilod = pupilod
        exam_.ca = ca
        exam_.caod = caod
        exam_.exam = exam
        exam_.save()
        messages.success(request, 'Les Examens ont été mises à jours avec succès!')
        return redirect('/listexam')
    exam = Exam.objects.get(id=id)
    context = {"exam":exam}
    return render(request,'home/editexam.html',context)

@login_required(login_url="/login/")
def deletexam(request,id):
    obj = get_object_or_404(Exam, id=id)
    obj.delete()
    return redirect('/listexam')






@login_required(login_url="/login/")
def creatediagnostique(request):
    if request.method == 'POST':
        diagnumdoss=request.POST.get('diagnumdoss')
        diagnostiqueog=request.POST.get('diagnostiqueog')
        diagnostiqueod=request.POST.get('diagnostiqueod')
        commentairediag=request.POST.get('commentairediag')
        check_existing =Diagnostique.objects.filter(diagnumdoss=diagnumdoss).exists()
        if check_existing:
            messages.error(request, 'Le numero de dossier existe deja!')
            return redirect('/creatediagnostique')
        else:
            query = Diagnostique(diagnumdoss=diagnumdoss,diagnostiqueog=diagnostiqueog,diagnostiqueod=diagnostiqueod,commentairediag=commentairediag)
            query.save()
            messages.success(request, 'Les Diagnostiques ont été enregistrés avec succès!')
            return redirect('/listdiagnostique')
    else:
        return render(request, 'home/savediagnostic.html')

@login_required(login_url="/login/")
def listdiagnostique(request):
    diag_list = Diagnostique.objects.all()
    paginator = Paginator(diag_list,100000000000)
    page = request.GET.get('page')
    try:
        diagnostiques = paginator.page(page)
    except PageNotAnInteger:
        diagnostiques = paginator.page(1)
    except EmptyPage:
        diagnostiques = paginator.page(paginator.num_pages)
    return render(request, 'home/listdiagnostic.html', {'diagnostiques': diagnostiques})


@login_required(login_url="/login/")
def editdiagnostique(request, id):
    diagnostique = Diagnostique.objects.get(id=id)
    context = {'diagnostique': diagnostique}
    return render(request, 'home/editdiagnostic.html', context)


@login_required(login_url="/login/")
def updatediagnostique(request, id):
    if request.method == 'POST':
        diagnumdoss=request.POST.get('diagnumdoss')
        diagnostiqueog=request.POST.get('diagnostiqueog')
        diagnostiqueod=request.POST.get('diagnostiqueod')
        commentairediag=request.POST.get('commentairediag')
        diagnostique = Diagnostique.objects.get(id=id)
        diagnostique.diagnumdoss=diagnumdoss
        diagnostique.diagnostiqueod=diagnostiqueod
        diagnostique.diagnostiqueog=diagnostiqueog
        diagnostique.commentairediag=commentairediag
        diagnostique.save()
        messages.success(request, 'Les Diagnostique ont été mises à jours avec succès!')
        return redirect('/listdiagnostique')
    diag = Diagnostique.objects.get(id=id)
    context = {"diag":diag}
    return render(request,'home/editdiagnostic.html',context)


@login_required(login_url="/login/")
def deletediagnostique(request,id):
    obj = get_object_or_404(Diagnostique, id=id)
    obj.delete()
    return redirect('/listdiagnostique')


@login_required(login_url="/login/")
def createtraitement(request):
    if request.method == 'POST':
        traitnumdoss=request.POST.get('traitnumdoss')
        traiteencours=request.POST.get('traiteencours')
        ccl=request.POST.get('ccl')
        cat=request.POST.get('cat')
        suivi_maladie=request.POST.get('suivi_maladie')
        dureelist=request.POST.getlist('duree')
        duree = ', '.join(dureelist)
        prescriptionlist=request.POST.getlist('prescription')
        prescription = ', '.join(prescriptionlist)
        doselist=request.POST.getlist('dose')
        dose = ', '.join(doselist)
        Tout_rdv=request.POST.get('Tout_rdv')
         # Create a copy of the request.POST QueryDict
        modified_data = QueryDict(request.POST.urlencode(), mutable=True)
        nompatienttr = modified_data.pop('nompatienttr', None)
        modified_data._mutable = False
        modified_data1 = QueryDict(request.POST.urlencode(), mutable=True)
        nommedecintr = modified_data1.pop('nommedecintr', None)
        modified_data1._mutable = False
        check_existing =Traitement.objects.filter(traitnumdoss=traitnumdoss).exists()
        if check_existing:
            messages.error(request, 'Le numero de dossier existe deja!')
            return redirect('/createtraitement')
        else:
            query = Traitement(duree=duree,prescription=prescription,dose=dose,traitnumdoss=traitnumdoss,traiteencours=traiteencours,ccl=ccl,cat=cat,suivi_maladie=suivi_maladie,Tout_rdv=Tout_rdv)
            query.save()
            messages.success(request, 'Les Traitements ont été enregistrés avec succès!')
            return redirect('/listtraitement')
    else:
        return render(request, 'home/savetraitement.html')
    
    
@login_required(login_url="/login/")
def listtraitement(request):
    trait_list = Traitement.objects.all()
    paginator = Paginator(trait_list,100000000000)
    page = request.GET.get('page')
    try:
        traitements = paginator.page(page)
    except PageNotAnInteger:
        traitements = paginator.page(1)
    except EmptyPage:
        traitements = paginator.page(paginator.num_pages)
    return render(request, 'home/listtraitement.html', {'traitements': traitements})


@login_required(login_url="/login/")
def edittraitement(request, id):
    traitement = Traitement.objects.get(id=id)
    context = {'traitement': traitement}
    return render(request, 'home/edittraitement.html', context)


@login_required(login_url="/login/")
def updatetraitement(request, id):
    if request.method == 'POST':
        traitnumdoss=request.POST.get('traitnumdoss')
        traiteencours=request.POST.get('traiteencours')
        ccl=request.POST.get('ccl')
        cat=request.POST.get('cat')
        suivi_maladie=request.POST.get('suivi_maladie')
        Tout_rdv=request.POST.get('Tout_rdv')
        dureelist=request.POST.getlist('duree')
        duree = ', '.join(dureelist)
        prescriptionlist=request.POST.getlist('prescription')
        prescription = ', '.join(prescriptionlist)
        doselist=request.POST.getlist('dose')
        dose = ', '.join(doselist)
        traitement = Traitement.objects.get(id=id)
        traitement.traitnumdoss = traitnumdoss
        traitement.traiteencours= traiteencours
        traitement.ccl=ccl
        traitement.cat=cat
        traitement.suivi_maladie=suivi_maladie
        traitement.Tout_rdv=Tout_rdv
        traitement.duree=duree
        traitement.prescription=prescription
        traitement.dose=dose
        traitement.save()
        messages.success(request, 'Les Traitements ont été enregistrés avec succès!')
        return redirect('/listtraitement')
    trait = Traitement.objects.get(id=id)
    context = {"trait":trait}
    return render(request,'home/edittraitement.html',context)



@login_required(login_url="/login/")
def deletetraitement(request,id):
    obj = get_object_or_404(Traitement, id=id)
    obj.delete()
    return redirect('/listtraitement')


from django.db import connection
@login_required(login_url="/login/")
def affichertout(request):
     with connection.cursor() as cursor:
        cursor.execute(""" SELECT i.* ,o.*,ate.*,e.*,em.*,d.*,tr.*
FROM chuybd.home_identification i 
LEFT JOIN chuybd.home_observation o
ON i.numerodossier = o.obsnumdoss
LEFT JOIN chuybd.home_antecedent ate
ON i.numerodossier = ate.atcdnumdoss
LEFT JOIN chuybd.home_enquete_system e
ON i.numerodossier = e.es_num_doss
LEFT JOIN chuybd.home_exam em 
ON i.numerodossier = em.examnumdoss
LEFT JOIN chuybd.home_diagnostique d
ON i.numerodossier = d.diagnumdoss
LEFT JOIN chuybd.home_traitement tr
ON i.numerodossier = tr.traitnumdoss; """)
        results = cursor.fetchall()
        context = {'results':results}
        return render(request, 'home/informationcomplet.html', context)





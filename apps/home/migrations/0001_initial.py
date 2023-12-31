# Generated by Django 3.2.6 on 2023-10-14 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atcdpo', models.TextField(blank=True, null=True)),
                ('atcdfogl', models.CharField(max_length=255)),
                ('atcdnumdoss', models.IntegerField()),
                ('atcddmla', models.CharField(max_length=255)),
                ('atcdaller', models.CharField(max_length=255)),
                ('atcdco', models.CharField(max_length=255)),
                ('atcdce', models.CharField(max_length=255)),
                ('atcdfammedhta', models.CharField(max_length=255)),
                ('atcdfamdiab', models.CharField(max_length=255)),
                ('atcdfamavc', models.CharField(max_length=255)),
                ('comatcdfammed', models.TextField(blank=True, null=True)),
                ('comatcdfammedical', models.TextField(blank=True, null=True)),
                ('fumeur', models.CharField(blank=True, max_length=255, null=True)),
                ('alcool', models.CharField(blank=True, max_length=255, null=True)),
                ('ordinateur', models.CharField(blank=True, max_length=255, null=True)),
                ('fdb', models.CharField(blank=True, max_length=255, null=True)),
                ('lunettes', models.CharField(blank=True, max_length=255, null=True)),
                ('medicaments', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnumdoss', models.IntegerField()),
                ('diagnostiqueog', models.CharField(blank=True, max_length=255, null=True)),
                ('diagnostiqueod', models.CharField(blank=True, max_length=255, null=True)),
                ('commentairediag', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enquete_System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_num_doss', models.IntegerField()),
                ('douleur', models.CharField(blank=True, max_length=255, null=True)),
                ('larme', models.CharField(blank=True, max_length=255, null=True)),
                ('picco', models.CharField(blank=True, max_length=255, null=True)),
                ('prurit', models.CharField(blank=True, max_length=255, null=True)),
                ('grains', models.CharField(blank=True, max_length=255, null=True)),
                ('visuels', models.CharField(blank=True, max_length=255, null=True)),
                ('meta', models.CharField(blank=True, max_length=255, null=True)),
                ('photopsies', models.CharField(blank=True, max_length=255, null=True)),
                ('myodesopsies', models.CharField(blank=True, max_length=255, null=True)),
                ('Cephalees', models.CharField(blank=True, max_length=255, null=True)),
                ('Otalgie', models.CharField(blank=True, max_length=255, null=True)),
                ('acouphene', models.CharField(blank=True, max_length=255, null=True)),
                ('nausees', models.CharField(blank=True, max_length=255, null=True)),
                ('vomissement', models.CharField(blank=True, max_length=255, null=True)),
                ('asthme', models.CharField(blank=True, max_length=255, null=True)),
                ('rhinorrhee', models.CharField(blank=True, max_length=255, null=True)),
                ('autrees', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examnumdoss', models.IntegerField()),
                ('inspection', models.CharField(blank=True, max_length=255, null=True)),
                ('reflets', models.CharField(blank=True, max_length=255, null=True)),
                ('cornee', models.CharField(blank=True, max_length=255, null=True)),
                ('corneeod', models.CharField(blank=True, max_length=255, null=True)),
                ('occulomotricite', models.CharField(blank=True, max_length=255, null=True)),
                ('ca', models.CharField(blank=True, max_length=255, null=True)),
                ('caod', models.CharField(blank=True, max_length=255, null=True)),
                ('avog', models.IntegerField(blank=True, null=True)),
                ('avod', models.IntegerField(blank=True, null=True)),
                ('piog', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('piod', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('sphereog', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('cylindreog', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('axeog', models.IntegerField(blank=True, null=True)),
                ('sphereod', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('cylindreod', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('axeod', models.IntegerField(blank=True, null=True)),
                ('cdvaleur', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('annexes', models.CharField(blank=True, max_length=255, null=True)),
                ('annexesod', models.CharField(blank=True, max_length=255, null=True)),
                ('iris', models.CharField(blank=True, max_length=255, null=True)),
                ('irisod', models.CharField(blank=True, max_length=255, null=True)),
                ('cristallin', models.CharField(blank=True, max_length=255, null=True)),
                ('cristallinod', models.CharField(blank=True, max_length=255, null=True)),
                ('vitre', models.CharField(blank=True, max_length=255, null=True)),
                ('vitreod', models.CharField(blank=True, max_length=255, null=True)),
                ('retine', models.CharField(blank=True, max_length=255, null=True)),
                ('retineod', models.CharField(blank=True, max_length=255, null=True)),
                ('macula', models.CharField(blank=True, max_length=255, null=True)),
                ('papille', models.CharField(blank=True, max_length=255, null=True)),
                ('exam', models.TextField(blank=True, null=True)),
                ('pupil', models.TextField(blank=True, null=True)),
                ('pupilod', models.TextField(blank=True, null=True)),
                ('nompatient', models.CharField(editable=False, max_length=255, null=True)),
                ('nommedecin', models.CharField(editable=False, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerodossier', models.IntegerField()),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('genre', models.CharField(max_length=7)),
                ('etatcivil', models.CharField(max_length=40)),
                ('profession', models.CharField(max_length=40)),
                ('dateconsultation', models.DateField(verbose_name='%m/%d/%Y')),
                ('telephone', models.CharField(max_length=14)),
                ('assurer', models.CharField(max_length=3)),
                ('assurancesocial', models.CharField(blank=True, max_length=40)),
                ('nomassureur', models.CharField(blank=True, max_length=40)),
                ('domicile', models.CharField(max_length=40)),
                ('regionorigine', models.CharField(max_length=20)),
                ('statutmalade', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motifcon', models.CharField(max_length=255)),
                ('poids', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('obsnumdoss', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Traitement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traitnumdoss', models.IntegerField()),
                ('traiteencours', models.TextField(blank=True, null=True)),
                ('ccl', models.CharField(blank=True, max_length=255, null=True)),
                ('cat', models.TextField(blank=True, null=True)),
                ('suivi_maladie', models.TextField(blank=True, max_length=255, null=True)),
                ('Tout_rdv', models.TextField(blank=True, null=True)),
                ('duree', models.CharField(blank=True, max_length=255, null=True)),
                ('prescription', models.CharField(blank=True, max_length=255, null=True)),
                ('dose', models.CharField(blank=True, max_length=255, null=True)),
                ('nompatienttr', models.CharField(editable=False, max_length=255, null=True)),
                ('nommedecintr', models.CharField(editable=False, max_length=255, null=True)),
            ],
        ),
    ]

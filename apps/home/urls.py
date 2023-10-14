

from django.urls import path as url, re_path
from apps.home import views
from django.contrib import admin

urlpatterns = [

    # The home page
    url('admin/', admin.site.urls),          # Django admin route
    url('', views.index, name='home'),
    url('createidentification', views.createidentification, name='createidentification'),
    url('listidentification', views.listidentification, name='listidentification'),
    url('editidentification/<int:id>', views.editidentification, name='editidentification'),
    url('updateidentification/<int:id>', views.updateidentification, name='updateidentification'), 
    url('deleteidentification/<int:id>', views.deleteidentification, name='deleteidentification'),
    url('createobservation', views.createobservation, name='createobservation'),
    url('listobservation', views.listobservation, name='listobservation'),
    url('editobservation/<int:id>', views.editobservation, name='editobservation'),
    url('updateobservation/<int:id>', views.updateobservation, name='updateobservation'), 
    url('deleteobservation/<int:id>', views.deleteobservation, name='deleteobservation'),
    url('createatcd', views.createatcd, name='createatcd'),
    url('listatcd', views.listatcd, name='listatcd'),
    url('editatcd/<int:id>', views.editatcd, name='editatcd'),
    url('updateatcd/<int:id>', views.updateatcd, name='updateatcd'), 
    url('deleteatcd/<int:id>', views.deleteatcd, name='deleteatcd'),
    url('createenquetesystem', views.createenquetesystem, name='createenquetesystem'),
    url('listenquetesysteme', views.listenquetesysteme, name='listenquetesysteme'),
    url('editenquetes/<int:id>', views.editenquetes, name='editenquetes'),
    url('updateenquetes/<int:id>', views.updateenquetes, name='updateenquetes'), 
    url('deleteenquetes/<int:id>', views.deleteenquetes, name='deleteenquetes'),
    url('createexam', views.createexam, name='createexam'),
    url('listexam', views.listexam, name='listexam'),
    url('editexam/<int:id>', views.editexam, name='editexam'),
    url('updateexam/<int:id>', views.updateexam, name='updateexam'), 
    url('deletexam/<int:id>', views.deletexam, name='deletexam'),
    url('creatediagnostique', views.creatediagnostique, name='creatediagnostique'),
    url('listdiagnostique', views.listdiagnostique, name='listdiagnostique'),
    url('editdiagnostique/<int:id>', views.editdiagnostique, name='editdiagnostique'),
    url('updatediagnostique/<int:id>', views.updatediagnostique, name='updatediagnostique'), 
    url('deletediagnostique/<int:id>', views.deletediagnostique, name='deletediagnostique'),
    url('createtraitement', views.createtraitement, name='createtraitement'),
    url('listtraitement', views.listtraitement, name='listtraitement'),
    url('edittraitement/<int:id>', views.edittraitement, name='edittraitement'),
    url('updatetraitement/<int:id>', views.updatetraitement, name='updatetraitement'), 
    url('deletetraitement/<int:id>', views.deletetraitement, name='deletetraitement'),
    url('affichertout', views.affichertout, name='affichertout'),
   
   
   
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

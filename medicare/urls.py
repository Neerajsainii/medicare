from django.contrib import admin
from django.urls import path
# from django.contrib.auth.decorators import login_required
# from django.conf.urls import handler404  
# from medicare import views
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", views.home),
    # path("info/", views.info),    
    # path('symptom/', views.symptom,name='symptom'),
    # path('disease/', views.process_symptom, name='disease'),
    # path('get_suggestions/', views.get_suggestions, name='get_suggestions'),
    # path('get_symptoms/<int:disease_id>/', views.get_symptoms,name='get_symptoms'),
    # path('medicine/<int:disease_id>/', views.treatment, name='medicine'),
    

]
# handler404 = 'Home.vieew.custom_404'
    
    
    
    # path("contact/", client_views.contact, name="contact"),
    # path("", medicalpractitioner_views.home, name="home"),
    # path("404/", medicalpractitioner_views.custom_404),
    # path("about/", medicalpractitioner_views.about, name="about"),
    # path("emergency/", medicalpractitioner_views.emergency, name="emergency"),
    # path("symptom/", medicalpractitioner_views.Symptom, name="symptom"),
    # path("infant/", medicalpractitioner_views.infant, name="infant"),
    # path("child/", medicalpractitioner_views.child, name="child"),
    # path("bmi/", medicalpractitioner_views.bmi, name="bmi"),
    # path("precaution/", medicalpractitioner_views.precaution, name="precaution"),


    #     path("w/", login_required(medicalpractitioner_views.whome), name="whome"),
    # path("wabout/", login_required(medicalpractitioner_views.wabout), name="wabout"),
    # path("wcontact/", login_required(medicalpractitioner_views.wcontact), name="wcontact"),
    # path("wemergency/", login_required(medicalpractitioner_views.wemergency), name="wemergency"),
    # path("wsymptom/", login_required(medicalpractitioner_views.wSymptom), name="wsymptom"),
    # path("wsymptoms/", login_required(medicalpractitioner_views.wsymptoms), name="wsymptoms"),
    # # path("wtreatment/", login_required(medicalpractitioner_views.wtreatment), name="wtreatment"),
    # # path("wdisease/", login_required(medicalpractitioner_views.wdisease), name="wdisease"),
    # path("wprecaution/", login_required(medicalpractitioner_views.wprecaution), name="wprecaution"),
    # path("winfant/", login_required(medicalpractitioner_views.winfant), name="winfant"),
    # path("wchild/", login_required(medicalpractitioner_views.wchild), name="wchild"),
    # path("wbmi/", login_required(medicalpractitioner_views.wbmi), name="wbmi"),

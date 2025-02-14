from django.shortcuts import render,redirect
from Station_Essence.models import *
import datetime
import platform,json
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def change_os_chemin(url):
    return '\\'.join(url) if platform.platform()=='windows' else '/'.join(url)

dates=str(datetime.datetime.now().date())


def login_user(request):
    error = None
    if request.method=='POST':
        username = request.POST.get('user')
        passwd=request.POST.get('pwd')
        user = authenticate(request, username=username, password=passwd)
        if user:
            login(request,user)
            return redirect('dashs')
        else:
            error = "Données incorrectes ! Veuillez réessayer"     
    return render(request,'login.html', context={"error":error})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

#les différents tableau de bord du projet global et de la station 
@login_required
def dash(request):
    return render(request,change_os_chemin(['dashboard','index.html']))


@login_required
def dash_essens(request):
    cuves=Special_cuve.objects.all()
    
     
    lec={}        
    with open('constantes.json', 'r') as fic:
            lec=json.load(fic)
            
    class dico_veil():
            def __init__(self,types):
                self.veil=Essence.objects.filter(type=types).last().jour
    
    
    if request.method=='POST':
        
            data={'prix_super':request.POST.get('prix_sup'),'prix_gazoil':request.POST.get('prix_gaz')}
            with open('constantes.json', 'w') as fic:
                json.dump(data,fic)
            
 
    total_sups=[dico_veil('Super1').veil,dico_veil('Super2').veil,dico_veil('Super3').veil,dico_veil('Super4').veil] 
    total_sups=sum(total_sups)
   
    total_gaz=[dico_veil('Gazoil1').veil,dico_veil('Gazoil2').veil,dico_veil('Gazoil3').veil,dico_veil('Gazoil4').veil,dico_veil('Gazoil5').veil,dico_veil('Gazoil6').veil]
    total_gaz=sum(total_gaz)
    
    valsup=total_sups*int(lec['prix_super'])
    valgaz=total_gaz*int(lec['prix_gazoil'])
    
    mairie=Mairie.objects.all()
    
    
    
    veil_gaz=mairie.filter(type='Gazoil').last()

    veil_sup=mairie.filter(type='Super').last()
    
    
    somme_total_mairie=veil_gaz.jour*int(lec['prix_gazoil']) + veil_sup.jour*int(lec['prix_super'])
    litres_total_mairie=veil_gaz.jour + veil_sup.jour  
    return render(request,change_os_chemin(['dashboard_essence','index.html']),
                  {'total_sup':total_sups,'total_mairie_som':somme_total_mairie,
                   'total_mairie_lit':litres_total_mairie,
                   'valgaz':valgaz,'total_gaz':total_gaz,
                   'valsup':valsup,'prix':lec,
                   'cuves':cuves})






            
            

#Essence composé de super et gazoil
@login_required
def essence(request):
    somme_j=0
    somme_v=0
    typ=""
    nom=0
    liste={}
    liste_sp=[]
    lec={}        
    default=''
    
    cuves=Special_cuve.objects.all()
    
    with open('constantes.json', 'r') as fic:
            lec=json.load(fic) 
    class dico_veil():
            def __init__(self,types):
                self.veil=Essence.objects.filter(type=types)
                
    
        
        
    
    def calcul_save(inti,types):
       
        print(types,int(request.GET.get('entrer')))   
        veil=Essence.objects.filter(type=types)
       
        if types[:3] == 'Sup':
            prix= int(lec['prix_super'])
        if types[:3] == 'Gaz':
            prix= int(lec['prix_gazoil'])
        
        gaz_save=Essence(
                    veille=veil.last().jour if veil.last() else int(request.GET.get('entrer')) ,
                    jour=veil.last().jour+int(request.GET.get('entrer')) if veil.last() else int(request.GET.get('entrer')),
                    quantite=int(request.GET.get('entrer')),
                    valeur=int(request.GET.get('entrer'))*prix,
                    date=datetime.datetime.now(),                   
                    type=types,
                )
        gaz_save.save()
              
        Special_cuv = get_object_or_404(Special_cuve, id=inti)       
        Special_cuv.quantite -= int(request.GET.get('entrer'))
        Special_cuv.save()
       

    if request.GET.get('ess')=="super" or request.GET.get('ess')[:3]=="Sup"  : 
          
        typ=request.GET.get('ess')     
        liste=[dico_veil('Super1'),dico_veil('Super2'),dico_veil('Super3'),dico_veil('Super4')] 
        liste_sp=liste  
        default=typ 
        
        if  request.GET.get('ess')[:3]=='Sup':
            liste_sp=dico_veil(typ)                    
            somme_v=liste_sp.veil.last().veille*int(lec['prix_super'])  if liste_sp.veil.last() else 0
            somme_j=liste_sp.veil.last().jour*int(lec['prix_super'])    if liste_sp.veil.last() else 0
            typ=request.GET.get('ess')[:3]                   
            nom=1
            
        if request.GET.get('entrer'):
            typ=request.GET.get('ess')         
            print(request.GET.get('entrer'))
            if typ=='Super1' or typ=='Super2':
                calcul_save(1,typ) 
            else:
                calcul_save(2,typ) 
            liste_sp=dico_veil(typ)                    
            somme_v=liste_sp.veil.last().veille*int(lec['prix_super'])
            somme_j=liste_sp.veil.last().jour*int(lec['prix_super'])
            cuves=Special_cuve.objects.all()

            
            
                     
    if request.GET.get('ess')=="gazoil" or request.GET.get('ess')[:3]=="Gaz" :  
        typ=request.GET.get('ess')
        liste=[dico_veil('Gazoil1'),dico_veil('Gazoil2'),dico_veil('Gazoil3'),dico_veil('Gazoil4'),dico_veil('Gazoil5'),dico_veil('Gazoil6')]
        liste_sp=liste
        default=typ
       
        if request.GET.get('ess')[:3]=='Gaz':
            liste_sp=dico_veil(typ)
            somme_v=liste_sp.veil.last().veille*int(lec['prix_super']) if liste_sp.veil.last() else 0
            somme_j=liste_sp.veil.last().jour*int(lec['prix_super']) if liste_sp.veil.last() else 0          
            nom=2
            typ=request.GET.get('ess')[:3]    
                           
        if request.GET.get('entrer'):
            typ=request.GET.get('ess')         
            calcul_save(3,typ)             
            liste_sp=dico_veil(typ)                    
            somme_v=liste_sp.veil.last().veille*int(lec['prix_super'])
            somme_j=liste_sp.veil.last().jour*int(lec['prix_super'])
            cuves=Special_cuve.objects.all()

    return render(request,change_os_chemin(['dashboard_essence','Essence.html']),
                  {'veilles':liste,'num':nom,
                   'type':typ,'default':default,
                   "liste_sp":liste_sp,'prix':lec,
                   'somme_v':somme_v,'somme_j':somme_j,
                   'cuve':cuves,'dates':dates,
                   })



#les différents parties du dashboard
@login_required
def entete(request):
    
    return render(request,change_os_chemin(['dashboard_essence','header.html']))

def navbar(request):
    
    return render(request,change_os_chemin(['dashboard_essence','navbar.html']))

def footer(request):
    return render(request,change_os_chemin(['dashboard_essence','footer.html']))







#la mairie 
@login_required
def mairie(request):
    mairie=Mairie.objects.all()
    lec={}        
    with open('constantes.json', 'r') as fic:
            lec=json.load(fic) 
            
            
    
        
    
    
    if request.method=="POST":
        if request.POST.get('prix_sup'):
            data={'prix_super':request.POST.get('prix_sup'),'prix_gazoil':request.POST.get('prix_gaz')}
            with open('constantes.json', 'w') as fic:
                json.dump(data,fic)
        if request.POST.get('input_maire'):
            quant=int(request.POST.get('input_maire'))
            
            
          
            
            if request.POST.get('choice')=='Gazoil':
                veil=mairie.filter(type='Gazoil').last()
                tarif=int(lec['prix_gazoil'])
                
            if request.POST.get('choice')=='Super':
                veil=mairie.filter(type='Super').last()
                tarif=int(lec['prix_gazoil'])
                
            Mairie_save=Mairie(
                    veille=veil.jour,
                    jour=veil.jour+quant,
                    quantite=quant,
                    valeur=quant*tarif,
                    date=datetime.datetime.now(),
                    type=request.POST.get('choice'),
                    type_pay=request.POST.get('type_pay'),
                   
                )
            Mairie_save.save()
            
    veil_gaz=mairie.filter(type='Gazoil').last()
    val_gaz=veil_gaz.jour*int(lec['prix_gazoil']) 
    veil_sup=mairie.filter(type='Super').last()
    val_sup=veil_sup.jour*int(lec['prix_super']) 
    
    somme_total_mairie=veil_gaz.jour*int(lec['prix_gazoil']) + veil_sup.jour*int(lec['prix_super'])
    litres_total_mairie=veil_gaz.jour + veil_sup.jour
    dico_mairie={'valeur_gaz':val_gaz,'valeur_sup':val_sup,'litre':litres_total_mairie,'toto':somme_total_mairie,'prix':lec,'veilgaz':veil_gaz,'veilsup':veil_sup,}
            
            
            
                      
    return render(request,change_os_chemin(['Mairie','mairie.html']),{'all_mairie':mairie,'aff_mairie':dico_mairie,'prix':lec})







#la livraison
@login_required
def livraison(request):
    
    
    lec={}        
    with open('constantes.json', 'r') as fic:
            lec=json.load(fic) 
    livrer=Livraison.objects.all()
    
    def cuve(types):
        
        Special_cuv = get_object_or_404(Special_cuve, id=types)
               
        Special_cuv.quantite += int(request.POST.get('entrer'))
        
        Special_cuv.save()
        
        
            
    if request.method=="POST":
        
        if request.POST.get('prix_sup'):
            data={'prix_super':request.POST.get('prix_sup'),'prix_gazoil':request.POST.get('prix_gaz')}
            
            with open('constantes.json', 'w') as fic:
                json.dump(data,fic)
        if request.POST.get('entrer'):
           
           choix=request.POST.get('choice')
           
           if choix=="Super 1" :
               prix=int(lec['prix_super'])
               cuve(1)
               

           elif choix=="Super 2":
               prix=int(lec['prix_super'])
               cuve(2)

           else :
               prix=int(lec['prix_gazoil'])
               cuve(3)
              
               
           save_livre=Livraison(
                quantite=int(request.POST.get('entrer')),
                valeur=int(request.POST.get('entrer'))*prix,
                date=datetime.datetime.now().date(),
                Cuve=request.POST.get('choice'),
           )
           save_livre.save()
         
    
     
    return render(request,change_os_chemin(['LIvraison','livraison.html']),
                  {'all_livraison':livrer,'cuvesuper1':livrer.filter(Cuve='Super 1'), 
                  'cuvesuper2':livrer.filter(Cuve='Super 2'),
                'cuvesgazoil':livrer.filter(Cuve='Gazoil'),
                'prix':lec,
                })



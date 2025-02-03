from django.shortcuts import render,redirect
from Station_Essence.models import *
import datetime
import platform,json
#Pour s'identifier avant d'entrée dans le dashboad


def change_os_chemin(url):
    return '\\'.join(url) if platform.platform()=='windows' else '/'.join(url)
dates=str(datetime.datetime.now().date())
def login(request):
    admin=request.POST.get('user')
    passwd=request.POST.get('pwd')
    if request.method=='POST':
        forms=User.objects.all()    
        for use in forms :
                print('ici')
                if use.Identifiant==admin and use.Password==passwd:
                    return redirect('dashs')
                elif use.Identifiant!=admin and use.Password==passwd :
                    return render(request,"login.html",context={"error1":1})
                elif use.Password!=passwd and use.Identifiant==admin:
                    return render(request,"login.html",context={"error2":1})
                else:
                    return render(request,"login.html",context={"error2":1,"error1":1})
                
    return render(request,'login.html')

#les différents tableau de bord du projet global et de la station essence
def dash(request):
    return render(request,change_os_chemin(['dashboard','index.html']))

def dash_essens(request):
    lec={}        
    with open('constantes.json', 'r') as fic:
            lec=json.load(fic)
    class dico_veil():
        def __init__(self,types):
            self.veil=Super.objects.filter(type=types).last().jour
    
    if request.method=='POST':
        
            data={'prix_super':request.POST.get('prix_sup'),'prix_gazoil':request.POST.get('prix_gaz')}
            with open('constantes.json', 'w') as fic:
                json.dump(data,fic)
            
    print(dico_veil(1).veil)   
    total_sups=[dico_veil(1).veil,dico_veil(2).veil,dico_veil(3).veil,dico_veil(4).veil]
    total_sups=sum(total_sups)
    class dico_veil():
        def __init__(self,types):
            self.veil=Gazoil.objects.filter(type=types).last().jour
    total_gaz=[dico_veil(1).veil,dico_veil(2).veil,dico_veil(3).veil,dico_veil(4).veil,dico_veil(5).veil,dico_veil(6).veil]
    total_gaz=sum(total_gaz)
    valsup=total_sups*int(lec['prix_super'])
    valgaz=total_gaz*int(lec['prix_gazoil'])
    mairie=Mairie.objects.all()
    
    
    
    veil_gaz=mairie.filter(type='Gazoil').last()
    val_gaz=veil_gaz.jour*int(lec['prix_gazoil'])
    veil_sup=mairie.filter(type='Super').last()
    val_sup=veil_sup.jour*int(lec['prix_super']) 
    
    somme_total_mairie=veil_gaz.jour*int(lec['prix_gazoil']) + veil_sup.jour*int(lec['prix_super'])
    litres_total_mairie=veil_gaz.jour + veil_sup.jour  
    return render(request,change_os_chemin(['dashboard_essence','index.html']),{'total_sup':total_sups,'total_mairie_som':somme_total_mairie,'total_mairie_lit':litres_total_mairie,'valgaz':valgaz,'total_gaz':total_gaz,'valsup':valsup,'prix':lec})






            
            

#les différents parties du dashboard
def essence(request):
    somme_j=0
    somme_v=0
    typ=""
    nom=0
    liste={}
    liste_sp=[]
    lec={}        
    default=''
    with open('constantes.json', 'r') as fic:
            lec=json.load(fic) 
    class dico_veil():
            def __init__(self,types):
                self.veil=Essence.objects.filter(type=types)
    
    def calcul_save(types):
        print('ici')
        print(types)   
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
        print('Bien Enregistrer')
        liste_sp=dico_veil(typ)                    
        somme_v=liste_sp.veil.last().veille*int(lec['prix_super'])
        somme_j=liste_sp.veil.last().jour*int(lec['prix_super'])

  
    if request.GET.get('ess')=="super" or request.GET.get('ess')[:3]=="Sup"  : 
        print('ici')   
        typ=request.GET.get('ess')     
        liste=[dico_veil('Super1'),dico_veil('Super2'),dico_veil('Super3'),dico_veil('Super4')] 
        liste_sp=liste  
        default=typ
        
        if  request.GET.get('ess')[:3]=='Sup':
            print('ici') 
            liste_sp=dico_veil(typ)                    
            somme_v=liste_sp.veil.last().veille*int(lec['prix_super'])  if liste_sp.veil.last() else 0
            somme_j=liste_sp.veil.last().jour*int(lec['prix_super'])    if liste_sp.veil.last() else 0
            typ=request.GET.get('ess')[:3]                   
            nom=1
            
        if request.GET.get('entrer'):
            print('ici_2')
            typ=request.GET.get('ess')
            calcul_save(typ)
            
            
                     
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
            calcul_save(typ)   
           
                     
      
     
    return render(request,change_os_chemin(['dashboard_essence','Essence.html']),{'veilles':liste,'num':nom,'type':typ,'default':default,"liste_sp":liste_sp,'prix':lec,'somme_v':somme_v,'somme_j':somme_j})









#les différents parties du dashboard
def entete(request):
    
    return render(request,change_os_chemin(['dashboard_essence','header.html']))

def navbar(request):
    
    return render(request,change_os_chemin(['dashboard_essence','navbar.html']))

def footer(request):
    return render(request,change_os_chemin(['dashboard_essence','footer.html']))

def gaz(request):
    return render(request,change_os_chemin(['dashboard_essence','essence_gaz.html']))
def sup(request):
    return render(request,change_os_chemin(['dashboard_essence','esssence_sup.html']))





           

    

    
# def super(request):  
#     supe=Super.objects.all()
    
#     somme_j=0
#     somme_v=0
#     var_sup=""


#     def calcul_save(types):
#         veil=Super.objects.filter(type=types).last().jour
#         supe_save=Super(
#                     veille=veil ,
#                     jour=veil+int(request.POST.get('super')) ,
#                     quantite=int(request.POST.get('super')),
#                     valeur=int(request.POST.get('super'))*int(lec['prix_super']),
#                     date=datetime.datetime.now(),
                    
#                     type=types,
#                 )
#         supe_save.save()
#         supe=Super.objects.filter(type=types)
            
            
        
#     class dico_veil():
#         def __init__(self,types):
#             self.veil=Super.objects.filter(type=types).last()
       
#     veils=[dico_veil(1),dico_veil(2),dico_veil(3),dico_veil(4)]
    
    
#     lec={}        
#     with open('constantes.json', 'r') as fic:
#             lec=json.load(fic) 
#     veil2=None
#     if request.method=='POST':
#         if request.POST.get('prix_sup'):
#             data={'prix_super':request.POST.get('prix_sup'),'prix_gazoil':request.POST.get('prix_gaz')}
    #         with open('constantes.json', 'w') as fic:
    #             json.dump(data,fic)
                
    #     make_get = False
       
    #     if request.POST.get('type'):
    #             veil2=request.POST.get('type')
    #             var_sup=int(request.POST.get('type'))
    #             make_get = True
              
    #     if make_get:
    #         supe=Super.objects.filter(type=var_sup)        
    #         somme_v=supe.last().veille*int(lec['prix_super'])
    #         somme_j=supe.last().jour*int(lec['prix_super'])
            
    #         if request.POST.get('super'):       
    #                 calcul_save(var_sup) 
    #                 somme_v=supe.last().veille*int(lec['prix_super'])
    #                 somme_j=supe.last().jour*int(lec['prix_super'])
            
    
    # return render(request,change_os_chemin(['Super','super.html']),{'all_super':supe,'num':veil2,'dates':dates,'sommej':somme_j,'sommev':somme_v,'veilles':veils,'prix':lec})



# #les pâges gazoils

# def gazoil(request):
#     var_sup=""
#     num=0
#     somme_j=0
#     somme_v=0
#     gazoil_table=Gazoil.objects.all()
    
    
#     if request.method=='POST':
#         if request.POST.get('prix_sup'):
#             data={'prix_super':request.POST.get('prix_sup'),'prix_gazoil':request.POST.get('prix_gaz')}
#             with open('constantes.json', 'w') as fic:
#                 json.dump(data,fic)
            
#     lec={}        
#     with open('constantes.json', 'r') as fic:
#             lec=json.load(fic)   
            
    
#     class dico_veil():
#         def __init__(self,types):
#             self.veil=Gazoil.objects.filter(type=types).last()
#     veils=[dico_veil(1),dico_veil(2),dico_veil(3),dico_veil(4),dico_veil(5),dico_veil(6)]
 
        
          
#     def calcul_save(types):
#             veil=Gazoil.objects.filter(type=types).last().jour
#             gaz_save=Gazoil(
#                     veille=veil,
#                     jour=veil+int(request.POST.get('gazoil')),
#                     quantite=int(request.POST.get('gazoil')),
#                     valeur=int(request.POST.get('gazoil'))*int(lec['prix_gazoil']),
#                     date=datetime.datetime.now(),                   
#                     type=types,
#                 )
#             gaz_save.save()
            
#             gazoil_table=Gazoil.objects.filter(type=types)
            
           
                
#     lec={}        
#     with open('constantes.json', 'r') as fic:
#             lec=json.load(fic) 
#     veil2=None
#     if request.method=='POST':
#         if request.POST.get('prix_sup'):
#             data={'prix_super':request.POST.get('prix_sup'),'prix_gazoil':request.POST.get('prix_gaz')}
#             with open('constantes.json', 'w') as fic:
#                 json.dump(data,fic)
                
#         make_get = False
       
#         if request.POST.get('type'):
#                 var_sup=request.POST.get('type')
#                 make_get = True
              
#         if make_get:
#             gazoil_table=Gazoil.objects.filter(type=var_sup)
#             veil2=gazoil_table.last()
#             somme_v=veil2.veille*int(lec['prix_gazoil'])
#             somme_j=veil2.jour*int(lec['prix_gazoil'])
            
#             if request.POST.get('gazoil'):
#                     calcul_save(var_sup) 
#                     veil2=gazoil_table.last()
#                     somme_v=veil2.veille*int(lec['prix_gazoil'])
#                     somme_j=veil2.jour*int(lec['prix_gazoil'])
                    
#     return render(request,change_os_chemin(['Gazoil','gazoil.html']),{'all_gazoil':gazoil_table,'num':veil2,'dates':dates,'sommej':somme_j,'sommev':somme_v,'veilles':veils,'prix':lec})
    

     

#la mairie 

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

def livraison(request):
    
    
    lec={}        
    with open('constantes.json', 'r') as fic:
            lec=json.load(fic) 
    livrer=Livraison.objects.all()
    
    if request.method=="POST":
        if request.POST.get('prix_sup'):
            data={'prix_super':request.POST.get('prix_sup'),'prix_gazoil':request.POST.get('prix_gaz')}
            with open('constantes.json', 'w') as fic:
                json.dump(data,fic)
        if request.POST.get('entrer'):
           
           choix=request.POST.get('choice')
           
           if choix=="Super 1" or choix=="Super 2":
               prix=int(lec['prix_super'])
           else :
               prix=int(lec['prix_gazoil'])
               
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


def sign(request):
    return render(request,'alert.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib
def index(request):

    donnees={
        'nom':'LUCIE',
        'postnom':'LUCIE',
        'sexe':'Feminin'
    }

    template=loader.get_template('index.html')
    return HttpResponse(template.render(donnees,request))

def listeEtudiants(request):
    return HttpResponse("Liste des etudiants")

def loyer(request):
    template=loader.get_template('ml.html')
    return HttpResponse(template.render({},request))

def predire(request):
    #on verifie si la methode est POST pour
    #recuperer les donnees du formulaire
    if request.method=='POST':

        #on garde dans les varialbes les valeurs
        #venues des champs du formulaire
        #on les convertit en entier car le formulaire
        #retourne par defaut les chaines de caracteres
        montant=int(request.POST['montant'])
        genre=int(request.POST['genre'])
        ponctialit=int(request.POST['ponctialit'])
        age=int(request.POST['age'])
        

        #on cree un table en deux dimensions pour le soumettre
        #au modele de prediction
        tableau=[[montant,genre,ponctialit,age]]
        print(tableau)

        #on charge le modele
        regresseur=joblib.load('modele_ml/model.pkl')
        resultat=regresseur.predict(tableau)
        
        print(resultat)
        return HttpResponse('ok')
    


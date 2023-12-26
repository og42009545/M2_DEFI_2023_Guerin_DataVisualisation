#J'importe le module csv 
import csv
from langdetect import detect
#J'ouvre le fichier 
eurovision = open("contestants.csv","r", encoding ="utf-8")
#Je charge les données issues du fichier 
lecteur = csv.reader(eurovision,  delimiter = ",")
#Je convertis en listes les données issues du fichier 
tableau = list(lecteur)
#Je ferme le fichier tp3_donnees.
eurovision.close()
for item in tableau:
    try:
        language = detect(item[11])
        item.append(language)
    except:
        language = "error"
        item.append(language)
#exporter le tableau dans un fichier csv dont le délimiteur est un \t
# j'ouvre le fichier à créer
fichier = open("liste_langue.csv","w", newline ="", encoding="utf-8")
#je spécifie le délimiteur voulu, ici tab
out = csv.writer(fichier)
#je remplis le fichier avec le contenu du tableau
for item in tableau :
        out.writerow(item)
#je ferme le fichier
fichier.close()
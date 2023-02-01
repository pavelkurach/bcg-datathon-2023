# Feuille de route

Objectif : optimizer la livraison 

Deux directions possibles :
- Livrer plus de colis en temps réduit 
- Réduire les couts de livraison 

## Livrable 1

En prenant en compte le taux moyen d'occupation, son écart type, l'impact des facteurs 
non-inclus dans le modèle, ainsi que l'erreur moyenne de prédiction, on peut 
s'attendre à la réduction du temps de livraison de 5 -- 15%. 

## Livrable 2

### Predictions à l'horizon d'une semaine

1. Prendre l'historique des livraisons ainsi que des données externes : 
- vacances
- fêtes
- confinements
- meteo
     
etc.

2. Construire grâce à ces données un **modèle de prediction des futures livraisons**. 

Algorithmes possibles:

- KMeans pour l'historique des livraisons
- LinearRegression, XGBoost, voire un réseau de neurones pour les données externes

3. Sur la base des predictions de ce modèle, découper la région parisienne en zones de livraison. 
Chaque zone correspond aux livraisons attribuées à un livreur. 

Chaque zone est caractérisée par plusieurs paramètres :

- Le nombre de livraisons en fonction de jour de la semaine / heure (*prédite par le modèle*)
- La surface de la zone

L'objectif est de choisir les créneaux avec le maximum de livraisons à effectuer et le minimum 
des coûts associés.

On peut définir les zones sur la base de l'équation suivante :

    Le nombre de livraisons effectué par un livreur = 
    = Surface de la zone × 'densité' des points de livraisons = 
    = 5 heures / temps de trajet moyen entre deux livraisons 

Le temps de trajet moyen entre deux livraisons se calcule grâce aux données historiques. 
Grâce à la réduction du temps de trajet de 5 -- 15%, la livraison sera faite en moins de 5 heures, 
mais en plus de 4 heures, et il y aura suffisamment d'écart pour terminer la livraison au cas où 
le taux d'occupation sera 50% plus élevé que prévu.

4. Sur la base des données utilisé pour la livrable 1, construire un **modèle de prediction de 
   trafic à court terme**.

Cela permettra une fois les addresses de livraisons attribuées à un livreur, d'optimiser son chemin.

### Les étapes d'optimisation

1. Grâce aux predictions des futures livraisons par zone, planifier les créneaux de livraison 
   et les attribuer aux livreurs. Cés créneaux doivent correspondre aux deadlines 
   imposés (une livraison tout les 2-3 jour par exemple) et maximiser le paramètre suivant :


    nombre de livraisons × (le revenu moyen par livraison -- le coût moyen de trajet entre 
deux 
    livraisons)

Le coût moyen de trajet  entre deux livraisons se calcule grâce au modèle de prédiction du 
traffic.

2. Une fois le livreur commence une livraison, utilisé les données de traffic les plus récentes 
   pour prédire le trafic dans les 5 prochaines heures et utiliser l'approche suivant pour 
   trouver le meilleur chemin entre les différentes adresses :

    
    to be completed
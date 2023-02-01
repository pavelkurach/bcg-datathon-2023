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

- La distance entre le point d'expédition et la zone
- La 'densité' des points de livraisons (*prédite par le modèle*)
- La surface de la zone 

L'objectif est de résoudre le problème d'optimisation : 
maximiser le nombre de livraisons et minimiser les couts. 

Les couts comprennent les couts associés au trajet entre le point d'expédition et la zone et les 
couts associés aux livraisons effectuées au sein de la zone.

On peut identifier deux types de zones :

- Les zones de type I avec le temps de trajet entre le point d'expédition et la zone est 
  inférieur à 1 heure (Paris). 

- Les zones de type I avec le temps de trajet entre le point d'expédition et la zone est 
  superior à 1 heure (banlieues). 

### Les zones de type I

La priorité est d'optimiser les livraisons au sein de la zone. La densité des points de 
livraisons doit être assez uniforme.

L'algorithme suivant propose une solution approximative :

    1. Definir les zones sur la base de l'equation suivante:
    Le nombre de livraisons effectué par un livreur = 
    = Surface de la zone $$\times$$ densité des points de livraisons = 
    = 5 heures / temps de trajet moyen entre deux livraisons 

Le temps de trajet moyen entre deux livraisons se calcule grâce aux données historiques. Grâce à 
la réduction du temps de trajet de 5 -- 15%, la livraison sera faite en moins de 5 heures, mais 
en plus de 4 heures, et il y aura suffisamment d'écart pour terminer la livraison au cas où le taux 
d'occupation sera 50% plus élevé que prévu. 

    2. Pour chaque zone et pour toutes les heures de livraison possibles, trouver le trajet qui 
    inclus tous les points de livraison est qui a le cout minimal. 

Pour cela, on peut considérer chaque zone comme un graphe ou les rues correspondent aux arrêts. 
En fonction de l'heure de livraison, on peut définir la distance entre les deux arrests comme le 
produit du coût horaire de livraison fois le temps de trajet prédit par le modèle. 

*Ainsi, on réduit le problème à la recherche du plus court chemin entre un ensemble de sommets 
dans un graphe.*

    3. Finalement, pour chaque zone selectionner l'heure de livraison avec le côut le livraison 
    minimale.

### Les zones de type II 

La priorité est d'optimiser le trajet entre le point d'expédition et la zone. 

La densité des points de livraison n'est pas uniforme, on peut découper la carte en clusters 
avec la densité plus élevée.

L'algorithme suivant propose une optimisation pour la livraison dans les zones de type II :

    1. Definir les zones comme des ensembles de clusters tels que le nombre de point de livraison 
    dans chaque zone est égal à 5 heures moins le temps de trajet entre le point d'expedition 
    est la zone divisés par le temps de trajet moyen entre deux livraisons 

Grâce à la réduction du temps de trajet de 5 -- 15%, la livraison sera faite en moins de 5 heures, mais 
en plus de 4 heures, et il y aura suffisamment d'écart pour terminer la livraison au cas où le taux 
d'occupation sera 50% plus élevé que prévu. 

    2. Pour chaque zone, trouver le temps de départ tels que le coût de trajet entre le point 
    d'expedition et la zone est minimal.

Finalement, on peut optimiser la livraison au sein de la zone de la même façon que pour les 
zones de type I.

    3. Pour chaque zone, trouver le trajet qui inclus tous les points de livraison est qui a le 
    cout minimal. 

### Résumé

Les algorithmes décrits ci-dessus permet à la fois d'augmenter le nombre de livraisons 
effectuées par un livreur dans un créneau de 4h à 8h, ainsi que réduire les coûts de trajet. 
Grâce à cela, on peut s'attendre à l'augmentation de revenue de 10-15%. 
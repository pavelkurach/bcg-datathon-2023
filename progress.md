## Task distribution:

- Parser – Саша + Петр + Фат ; result check 28 Jan 20:00
- Base line // data pre-processing – Рома ; till 28 Jan 20:00
- Github – Петр ; 1/2 hour
- Business solution part (une feuille de route de la suite du projet) -- Паша + Фат
- Presentation -- Паша + Фат


Questions: 

1. Do we merge datasets ? In this case how should we handle missing target data in the 2nd dataset?

2. How are we going to solve a Multi target regression problem? 

My thoughts: 

- firstly we should try to solve single regression problems using two approaches: direct (independent models) and chained (using first prediction as a feature for the second model). There are wrappers for these approaches. In this case we can merge all data (and try to handle the missing data problem for the chained approach) and then try and see results of separate data

- secondly we can explore some multi-output models cause they can take into account relationships between the target variables (it can give better results cause they are dependent in our case)   


<u>Question to ask tomorrow during atelier<\u>




## Progress:

Parser



Remarks:
## Base line



Remarks:


## Business solution part

Principal points:

- maximize the number of shipments on difined period of time
- minimize the cost 
- minimize carbon emission across the delivery process


Remarks:
## Presentation



Remarks:

## References:

[Временные ряды. Простые решения](https://habr.com/ru/post/553658/)

[Dataset](https://opendata.paris.fr/explore/dataset/comptages-routiers-permanents/export/?disjunctive.libelle&disjunctive.etat_trafic&disjunctive.libelle_nd_amont&disjunctive.libelle_nd_aval&sort=t_1h)



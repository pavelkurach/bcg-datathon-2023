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


<ins>Question to ask tomorrow during atelier</ins>

-


## Progress:

## Parser



Remarks:
## Base line



Remarks:


## Business solution part

Principal points:

- maximize the number of shipments on difined period of time
- minimize the cost 
- minimize carbon emission across the delivery process

1. Создаем граф так, чтобы ребра были улицами (отвечает за время преодоления этого маршрута). Граф зависит от времени.  Вводим расстояние между вершинами как произведение времени на поездку на цену за проведение операции. Зависит от времени. Разбиваем все заказы на кластеры, каждый из которых отвечает за рабочий день доставщика. Цель -- чтобы каждый кластер был оптимизирован и каждый заказ попал ровно в один кластер. 
2. Нужно получить набор для i-й доставки $$OS_j = [S_{j_1}, \dots, S_{j_n}]$$ список адресов, в которые приезжает доставщих (вершины графа). Хотим найти время этой доставки:
$$Time (OS_j) = \sum_{m=1}^n $$
$$Cost (OS_j) = \sum \dots$$

3. Цель: 

$$\text{min} \sum_{j=1}^N Cost(OS_j)$$
under constraints:
$$\forall j\in[1,\dots, N] \text{Time} (OS_j) \in [4, 8] $$
$$\forall s \in \text{Orders} \text{exist} j(s): s \in OS_{j(s)} $$


4.1. Вопрос -- мы знаем заказы заранее или нужно их предсказать. Доставлять то, что заказано или моделировать, что будет заказано? Перепрогонять алгоритм в случае новых заказов в течение недели?
4.2. Как эту задачу опитимизации решать? Посмотреть, есть ли статьи. 

5. Performance boosters: 
5.1. Учесть момент когда меняется шофер. Сколько времени тратится на вернуться - передать машину. 
5.2. Пусть есть квартал размером 1 км, находящийся в 20 км от центра. Нам гораздо важнее оптимизировать время, за которое мы проходим 20 км. Важно понять, в какой момент времени вырваться из условного центра и доехать до этого маленького отдалённого от центра района. 
Remarks:
## Presentation



Remarks:

## References:

[Временные ряды. Простые решения](https://habr.com/ru/post/553658/)

[Dataset](https://opendata.paris.fr/explore/dataset/comptages-routiers-permanents/export/?disjunctive.libelle&disjunctive.etat_trafic&disjunctive.libelle_nd_amont&disjunctive.libelle_nd_aval&sort=t_1h)



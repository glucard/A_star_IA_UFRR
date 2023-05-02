# python 3.11.2
from collections import defaultdict
import random


MIN_VISITED = 1
MAX_VISITED = 3

p_from = 'Brasil'
p_to = 'Japão'

places = [
    "Brasil",
    "Japão",
    "Canada",
    "Romenia",
    "Equador",
    "UFRR",
    "USA",
    "Praia",
]

done_places = []
avaliable_places = places.copy()

random.seed(1)

paths = defaultdict(dict)
while len(done_places) < len(places) :
    p0 = random.choice(avaliable_places)
    p1 = random.choice(avaliable_places)
    while p0 == p1:
        p1 = random.choice(avaliable_places)
    
    distance = random.randint(1,100)
    paths[p0][p1] = distance
    paths[p1][p0] = distance

    for p in [p0, p1]:
        if len(paths[p]) >= MAX_VISITED:
            avaliable_places.remove(p)
        if len(paths[p]) >= MIN_VISITED:
            if done_places.count(p) == 0:
                done_places.append(p)

print(paths)

hDLR = defaultdict(dict)
for p in places:
    distance = None
    if p == p_to:
        distance = 0

    elif p_to in paths[p].keys():
        distance = paths[p][p_to]
    
    elif distance == None:
        distance = random.randint(1,100)

    hDLR[p] = distance

print(hDLR)
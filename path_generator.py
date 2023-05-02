# python 3.11.2
# ! pip install matplotlib

from matplotlib import pyplot as plt
from collections import defaultdict
import random
import numpy as np

# params
MIN_VISITED = 1 # min node neighbors count
MAX_VISITED = 4 # max node neighbors count

p_from = 'Brasil' # start place
p_to = 'Japão' # destiny place


# all places names
places = [ 
    "Brasil",
    "Japão",
    "Canada",
    "Romenia",
    "Equador",
    "UFRR",
    "USA",
    "Praia",
    "Cuba",
    "Coreia do Sul",
]


# randomizing position of each place
position = {
    p: np.array((random.randint(0, 500), random.randint(0,500)))
    for p in places
}

done_places = []
avaliable_places = places.copy()

paths = defaultdict(dict)

# creating the connections between each place
while len(done_places) < len(places) :
    
    # random select the places to create a connection between nodes
    p0 = random.choice(avaliable_places)
    p1 = random.choice(avaliable_places)
    while p0 == p1:
        p1 = random.choice(avaliable_places)
    
    # calculate the distance of each point
    distance = np.linalg.norm(position[p1] - position[p0])

    # define the path and its distance
    paths[p0][p1] = distance
    paths[p1][p0] = distance

    # repeated the same for each previous nodes
    for p in [p0, p1]:
        # verify if the place already has the max neighbors count
        if len(paths[p]) >= MAX_VISITED:
            # if it has, then remove from places that have avaliable places to new neighbors
            avaliable_places.remove(p)
        # verify if the place already has the min neights count
        if len(paths[p]) >= MIN_VISITED:
            # if it has, then add it to accepted (done) places
            if p not in done_places:
                done_places.append(p)

# defining the heuristic ditansce between a ret line from the a place to destiny place
hDLR = defaultdict(dict)

# for each place
for p in places:

    distance = None
    # if the place is the destiny, then heuristic is 0
    if p == p_to:
        distance = 0
    
    # if the place is neighbors to the destiny, then heuristic is the distance between each one
    elif p_to in paths[p].keys():
        distance = paths[p][p_to]
    
    # if not in previous cases, then heuristic is the distance (norm) between each place
    else:
        distance = np.linalg.norm(position[p] - position[p_from])

    # store heuristic on its respective place
    hDLR[p] = distance


print(hDLR)


# just mapping the places using matplotlib for better visualization

# plot places
x, y = np.array([[x,y] for x,y in position.values()]).T
plt.scatter(x,y)

# plot connections lines between each place
for p0 in paths:
    for p1 in paths[p0]:
        line_x, line_y = np.array([position[p0],position[p1]]).T
        plt.plot(line_x, line_y, marker='o')

# plot places label
for i, txt in enumerate(places):
    plt.annotate(txt, (x[i], y[i]))

plt.show()
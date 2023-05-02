# not safe example of a* o.o
# python 3.11.2
# ! pip install matplotlib
from path_generator import paths, hDLR, p_from, p_to

# put the start node in open
open = [p_from]
open_g = [0]
closed = []

current_path = []

print(f'from {p_from} to {p_to}:')

while True:

    # if open is empty then exit with failure
    if len(open) == 0:
        print("ERROR")
        break
    
    # for the node that has the minimun f
    minf = float('inf')
    minf_n = None
    for i, n in enumerate(open):
        # f(n) = g(n) + h(n)
        f = open_g[i] + hDLR[n]
        if f < minf and n not in closed:
            minf = f
            minf_n = n

    # remove from open and place in closed a node n which f is minimum
    open_g.pop(open.index(minf_n))
    open.remove(minf_n)
    closed.append(minf_n)

    # add to current_path to keep track of the path
    current_path.append(minf_n)

    # if n is goal node then exit sucessfully
    if minf_n == p_to:
        print("SUCESSO")
        break
    
    # else expand n, generating all it sucessors, and attach them pointers back to n
    for next_n, g in paths[minf_n].items():
        open.append(next_n)
        open_g.append(g)

# solution obtained by tracking back the pointers from n to s
solution = []
for i in range(len(current_path)-1, 0, -1):
    if current_path[i-1] in paths[current_path[i]]:
        solution.insert(0, current_path[i-1])
solution.append(p_to)


# HERES YOUR SOLUTION, liro boi
print(solution)
from path_generator import paths, hDLR, p_from, p_to

open = [p_from]
closed = []

print(f'from {p_from} to {p_to}:')
while True:
    if len(open) == 0:
        print("ERROR")
        break

    minf = float('inf')
    minf_n = None
    for n in open:
        for next_n, distance in paths[n].items():
            f = distance + hDLR[next_n]
            if f < minf and next_n not in closed:
                minf = f
                minf_n = next_n
    
    print(minf, minf_n)
    if minf_n not in closed:
        open.append(minf_n)
        closed.append(minf_n)
    if all(i_n in closed for i_n in minf_n):
        open.remove(minf_n)
    if minf_n == p_to:
        print("SUCESSO")
        break
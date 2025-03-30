def kruskal():





V,E = map(int, input().split())
edges = []

for _ in range(E) :
    start, end, weight = map(int, input().split())
    edges.append((start,end,weight))

edges.sort(key=lambda x : x[2])

print(edges)
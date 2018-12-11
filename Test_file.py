from Graph import Graph, Vertex
import Algorithms
import time

start = time.time()

g = Graph()
# Taken from ZyBooks to test Topological Sort
vertex_A = Vertex('A')
vertex_B = Vertex('B')
vertex_C = Vertex('C')
vertex_D = Vertex('D')
vertex_E = Vertex('E')
vertex_F = Vertex('F')
vertex_G = Vertex('G')

g.add_vertex(vertex_A)
g.add_vertex(vertex_B)
g.add_vertex(vertex_C)
g.add_vertex(vertex_D)
g.add_vertex(vertex_E)
g.add_vertex(vertex_F)
g.add_vertex(vertex_G)

g.add_directed_edge(vertex_A, vertex_B)
g.add_directed_edge(vertex_A, vertex_C)
g.add_directed_edge(vertex_B, vertex_F)
g.add_directed_edge(vertex_C, vertex_D)
g.add_directed_edge(vertex_D, vertex_F)
g.add_directed_edge(vertex_E, vertex_F)
g.add_directed_edge(vertex_E, vertex_G)
g.add_directed_edge(vertex_F, vertex_G)

# Topological implementation to test from ZyBooks
result_list = Algorithms.topological_sort(g)
print("\n")
print("Topological Sort Algorithm from ZyBooks: ")

first = True
for vertex in result_list:
    if first:
        first = False
    else:
        print(' -> ', end='')  # separate vertex values
    print(vertex.label, end='')  # Print vertex values
print(" ")

# Kruskals implementation from ZyBooks
print("\n")
print("Kruskals Algorithm: ")
graph2 = dict(vertex=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],

              edges={(15, 'A', 'B'),
                     (6, 'A', 'D'),
                     (9, 'B', 'C'),
                     (12, 'B', 'D'),
                     (14, 'B', 'G'),
                     (10, 'B', 'H'),
                     (16, 'C', 'E'),
                     (8, 'D', 'E'),
                     (20, 'E', 'F')})

graph3 = dict(vertex=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'P'],

              edges={(80, 'A', 'B'),
                     (105, 'A', 'C'),
                     (182, 'A', 'E'),
                     (90, 'B', 'C'),
                     (60, 'B', 'D'),
                     (100, 'B', 'P'),
                     (132, 'C', 'P'),
                     (80, 'D', 'E'),
                     (70, 'E', 'F'),
                     (72, 'F', 'G'),
                     (145, 'F', 'P'),
                     (180, 'G', 'P')})


print("Minimal Spanning Tree of Graph 1 from ZyBooks: ", "\n", (Algorithms.kruskal(graph2)))
print("\n")
print("Minimal Spanning Tree of Graph 2 from ZyBooks: ", "\n", (Algorithms.kruskal(graph3)))

end = time.time()
print("\n")
print("Time it took to run through program: ", (end-start))

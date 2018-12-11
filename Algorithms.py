# Disjoint Set Forest taken from GraphAm
def disjoint_set(graph):  # Create sets for dsf
    sets[graph] = graph
    vertices[graph] = 0


def find(graph):  # Util function to help find subsets of graph
    if sets[graph] != graph:
        sets[graph] = find(sets[graph])
    return sets[graph]


def union(set1, set2):  # Util function to combine both sets
    ra = find(set1)
    rb = find(set2)

    if ra != rb:  # Iterates through conditionals to combine sets unless both sets have repeated elements
        if vertices[ra] > vertices[rb] or vertices[ra] < vertices[rb]:
            sets[rb] = ra

        if vertices[ra] == vertices[rb]:  # If vertices are the same then increment both vertices
            vertices[ra] += 1
            vertices[rb] += 1


# The Topological sort function is from ZyBook
def get_incoming_edge_count(edge_list, vertex):
    count = 0
    for (from_vertex, to_vertex) in edge_list:
        if to_vertex is vertex:
            count += 1
    return count


def topological_sort(graph):
    result_list = []

    e = []

    for vertex in graph.adjacency_list.keys():
        if get_incoming_edge_count(graph.edge_weights.keys(), vertex) == 0:
            e.append(vertex)

    remaining_edges = set(graph.edge_weights.keys())  # starts with all edges
    while len(e) is not 0:
        curr_vertex = e.pop()  # select next vertex
        result_list.append(curr_vertex)
        outgoing_edges = []

        # remove current vertex outgoing edges from remaining edges
        for to_vertex in graph.adjacency_list[curr_vertex]:
            outgoing_edge = (curr_vertex, to_vertex)

            if outgoing_edge in remaining_edges:
                outgoing_edges.append(outgoing_edge)
                remaining_edges.remove(outgoing_edge)

        # check if removing outgoing edges creates new vertices with no incoming edges
        for (from_vertex, to_vertex) in outgoing_edges:
            in_count = get_incoming_edge_count(remaining_edges, to_vertex)
            if in_count == 0:
                e.append(to_vertex)

    return result_list  # Return sorted topological list


sets = {}       # Create an empty set dict
vertices = {}   # Create an empty vertex dict


# Kruskals Algorithm Implementation
def kruskal(graph):
    # Global statements to help with the outer scope variable calls
    global dsf, tree_edges

    # Find the minimum spanning tree of the vertices
    for i in graph['vertex']:  # Vertex called in main
        # Use Util functions to help find min spanning tree
        disjoint_set(i)
        tree_edges = list(graph['edges'])  # Edges called in main
        tree_edges.sort()  # sort edges
        dsf = set()

    # Find the minimum spanning tree of the edges
    for j in tree_edges:
        w, vertex_set1, vertex_set2 = j  # Weight, vertex_1, vertex_2

        if find(vertex_set1) != find(vertex_set2):
            union(vertex_set1, vertex_set2)

            dsf.add(j)  # Add edge to dsf

    return sorted(dsf)  # Return sorted graph

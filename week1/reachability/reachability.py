#Uses python3
import sys

def number_of_components(adj, edge_to_find, visited_vertices=[], current_vertex=None, ):
    vertex1 = edge_to_find[0]
    vertex2 = edge_to_find[1]

    if current_vertex is None:
        current_vertex = vertex1
        print(f"current_vertex: {current_vertex}")

    if current_vertex == vertex2:
        return 1

    visited_vertices.append(current_vertex)
    print(f"visited_vertices: {visited_vertices}")

    print(f"adj[current_vertex]: {adj[current_vertex]}")
    next_vertices = [x for x in adj[current_vertex] if x not in visited_vertices]
    print(f"next_vertices: {next_vertices}")

    for next_vertex in next_vertices:
        print('---------------')
        print(f"visited_vertices: {visited_vertices}, next_vertex: {next_vertex}")
        print(f"adj: {adj}")
        print(f"edge_to_find: {edge_to_find}")
        return number_of_components(adj, edge_to_find, visited_vertices, next_vertex)

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]

    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    edge_to_find = data[-2:]
    edge_to_find = [ a-1 for a in edge_to_find ]

    edges = [ (a - 1, b - 1) for (a, b) in edges ]
    adj = [[] for _ in range(n)]

    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)

    print(number_of_components(adj, edge_to_find))

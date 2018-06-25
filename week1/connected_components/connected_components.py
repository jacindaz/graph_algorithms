#Uses python3
import sys

def visited_edges(all_adj_nodes):
    result = 0
    visited_nodes = []
    visited_edges = []

    print(f"all_adj_nodes: {all_adj_nodes}")

    for index, adj_nodes in enumerate(all_adj_nodes):
        print(f"----------------")
        print(f"adj_nodes: {adj_nodes}, index: {index}")
        print(f"visited_edges: {visited_edges}")
        print(f"visited_nodes: {visited_nodes}")

        current_index = index
        visited_nodes.append(current_index)

        if len(adj_nodes) == 0:
            visited_edges.append((current_index, None))
        else:
            for node in adj_nodes:
                print(f"node: {node}")
                sorted_visited_edge = sorted([current_index, node])
                print(f"sorted_visited_edge: {sorted_visited_edge}")

                edge_we_are_visiting = tuple(sorted_visited_edge)
                print(f"edge_we_are_visiting: {edge_we_are_visiting}")

                if edge_we_are_visiting not in visited_edges:
                    visited_edges.append(edge_we_are_visiting)
                    print(f"new visited edge: {visited_edges}")

    return visited_edges

def number_of_components(all_adj_nodes):
    adjacent_edges = visited_edges(all_adj_nodes)
    # print(f"adjacent_edges: {adjacent_edges}")
    connected_components = []

    return connected_components

# print(number_of_components([[1],[0,2],[1],[]])) # output: 2
# print(number_of_components([[1],[0,2,3],[1,3],[2,1,4],[3], []]))

# output: 2, connected components are: {4}, {1,2,3,5}
print(number_of_components([[1],[0,2,4],[1],[],[1]]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]

    print(f"data before: {data}")
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    print(f"edges after: {edges}")

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(f"adj: {adj}\n")
    print(number_of_components(adj))

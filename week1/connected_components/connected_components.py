#Uses python3
import sys

def number_of_components(all_adj_nodes):
    result = 0

    visited_nodes = []
    visited_edges = []

    for index, adj_nodes in enumerate(all_adj_nodes):
        print(f"----------------")
        print(f"adj_nodes: {adj_nodes}, index: {index}")
        print(f"visited_edges: {visited_edges}")
        print(f"visited_nodes: {visited_nodes}")

        current_index = index
        visited_nodes.append(current_index)

        for node in adj_nodes:
            print(f"node: {node}")
            sorted_visited_edge = sorted([current_index, node])
            print(f"sorted_visited_edge: {sorted_visited_edge}")

            edge_we_are_visiting = tuple(sorted_visited_edge)
            print(f"edge_we_are_visiting: {edge_we_are_visiting}")

            if edge_we_are_visiting not in visited_edges:
                visited_edges.append(edge_we_are_visiting)
                print(f"new visited edge: {visited_edges}")

    return len(visited_edges)

# print(number_of_components([[1],[0,2],[1], []]))
# print(number_of_components([[1],[0,2,3],[1,3],[2,1,4],[3], []]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(number_of_components(adj))

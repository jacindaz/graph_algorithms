#Uses python3
import sys
# import ipdb

def number_of_components(adj):
    result = 0

    visited = [0] * len(adj)
    for i in range(len(adj)):
        # print(f"\ni: {i}, visited[i]: {visited[i]}")
        # print(f"visited: {visited}, result: {result}")

        # if visited[i] == 0, runs the clause
        # if not visited[i]:
        if visited[i] == 0:
            # print(f"\ni: {i}, visited[i]: {visited[i]}")
            # print(f"visited: {visited}, result: {result}")

            explore(adj, i, visited)
            result += 1

            # print(f"visited updated: {visited}")
    return result


def explore(adj, node_index, visited):
    visited[node_index] = 1

    adjacent_nodes = adj[node_index]
    for current_adj_node in adjacent_nodes:
        current_node_visited = visited[current_adj_node]

        # print("------------")
        # print(f"current_adj_node: {current_adj_node}")
        # print(f"visited: {visited}")
        # print(f"current_node_visited: {current_node_visited}")
        if not current_node_visited:
            explore(adj, current_adj_node, visited)



# print(number_of_components([[1],[0,2],[1],[]])) # output: 2
# print(number_of_components([[1],[0,2,3],[1,3],[2,1,4],[3], []]))

# output: 2, connected components are: {4}, {1,2,3,5}
# print(number_of_components([[1],[0,2,4],[1],[],[1]]))
# print(explore([[1],[0,2,4],[1],[],[1]], 0, [0,0,0,0,0]))

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

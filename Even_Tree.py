"""
Hacker Rank Problem
Name: Even Tree
link: https://www.hackerrank.com/challenges/even-tree/problem

solution:
"""


# !/bin/python3


def make_tree(t_from, t_to):
    tree = {}
    for node1, node2 in zip(t_from, t_to):
        tree.setdefault(node1, []).append(node2)
        tree.setdefault(node2, []).append(node1)

    return tree


def is_even_nodes(tree, node, except_for):
    count = 1
    nodes = [node]
    nodes_visited = set([node])
    while nodes:
        cur_node = nodes.pop()
        for n in tree[cur_node]:
            if n != except_for and n not in nodes_visited:
                nodes_visited.add(n)
                count += 1
                nodes.append(n)

    return count % 2 == 0


def remove_edge(tree, node1, node2):
    tree[node1].remove(node2)
    tree[node2].remove(node1)


# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    tree = make_tree(t_from, t_to)
    removed_edge_count = 0
    i = 0
    while i != len(t_from):
        dist1 = is_even_nodes(tree, t_from[i], t_to[i])
        dist2 = is_even_nodes(tree, t_to[i], t_from[i])

        if dist1 and dist2:
            node1 = t_from.pop(i)
            node2 = t_to.pop(i)
            remove_edge(tree, node1, node2)
            i = 0
            removed_edge_count += 1

        else:
            i += 1

    return removed_edge_count



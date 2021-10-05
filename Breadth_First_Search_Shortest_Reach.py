"""
Hacker Rank Problem
Name: Breadth First Search: Shortest Reach
link: https://www.hackerrank.com/challenges/bfsshortreach/problem

solution:
"""
from collections import deque


def bfs(n, m, edges, s):
    results = [-1] * n
    results[s - 1] = 0
    tree = make_graph(edges, n)

    # Deque is python data structure implemented optimally to act both as
    # stack and queue where .pop(0) and .pop() both has O(1) time.
    bfs_q = deque([s])
    done_set = set([])

    while bfs_q:
        cur = bfs_q.popleft()
        done_set.add(cur)
        for node in tree[cur]:
            if node not in done_set:
                bfs_q.append(node)

                new_size = results[cur - 1] + 6
                if results[node - 1] == -1:
                    results[node - 1] = new_size
                else:
                    results[node - 1] = min(results[node - 1], new_size)

    results.pop(s - 1)
    return results


def make_graph(edges, n):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = set()

    for node1, node2 in edges:
        graph[node1].add(node2)
        graph[node2].add(node1)

    return graph


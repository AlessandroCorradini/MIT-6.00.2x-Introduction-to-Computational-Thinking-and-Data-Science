## Exercise 6

In the following examples, assume all graphs are undirected. That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.

A clique is an unweighted graph where each node connects to all other nodes. We denote the clique with  nodes as KN. Answer the following questions in terms of .

What is the asymptotic worst-case runtime of a Breadth First Search on KN? For simplicity, write  as just n, O(n^2) as n^2, etc.

n 
 
BFS will always run faster than DFS.

- True
- False [X]

If a BFS and DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), BFS will always run at least as fast as DFS when run on two nodes in KN.


- True [X]
- False

If a BFS and Shortest Path DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), BFS will always run at least as fast as Shortest Path DFS when run on two nodes in any connected unweighted graph.


- True [X]
- False

Regardless of node priority, BFS will always run at least as fast as Shortest Path DFS on two nodes in any connected unweighted graph.

- True [X]
- False
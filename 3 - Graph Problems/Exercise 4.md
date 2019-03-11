## Exercise 4

Consider our continuing problem of permutations of three students in a line. Use the enumeration we established when adding the nodes to our graph. That is,

```
nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]
```

so that ABC is Node 0, BCA is Node 3, etc.

Using Depth First Search, and beginning at the listed source nodes, give the first path found to the listed destination nodes. For the purpose of this exercise, assume DFS prioritizes lower numbered nodes. For example, if Node 2 is connected to Nodes 3 and 4, the first path checked will be 23. Additionally, DFS will never return to a node already in its path.

To denote a path, simply list the numbers of the nodes exactly as done in the lecture.

- Source: 0
- Destination: 4
- 014

<br/>

- Source: 4
- Destination: 1
- 41

<br/>

- Source: 1
- Destination: 1
- 1

<br/>

- Source: 2
- Destination: 4
- 2014

<br/>

- Source: 2
- Destination: 3
- 201453

<br/>

- Source: 3
- Destination: 1
- 3201

We saw before that for permutations of 3 people in line, any two nodes are at most three edges, or four nodes, away. But DFS has yielded paths longer than three edges! In this graph, given a random source and a random destination, what is the probability of DFS finding a path of the shortest possible length?


2/3
  
## Exercise 1

We often use graphs to simplify optimization problems, as they are easy implement on a computer.

The following concepts can be illustrated with a graph. Determine which variables should be represented by edges and vertices in this graph.

A school's course catalog

Some classes must occur at least one semester before certain other classes (e.g., Calculus I must be taken before Calculus II), but not all classes have prerequisites.

If we want to represent the catalog as a graph, which variables should be represented as edges and vertices?


- A) Each edge is a class, while different vertices indicate the semester the class is taken.
- B) Each vertex is a class, while a directional edge indicates that one class must come before another. [X]
- C) Each vertex is a class, while edges between two vertices indicate that the classes may be taken at the same time.

Students in a line

Second graders are lining up to go to their next class, but must be ordered alphabetically before they can leave. The teacher only swaps the positions of two students that are next to each other in line.

If we want to represent this situation as a graph, which variables should be represented as edges and vertices?


- A) Vertices represent permutations of the students in line. Edges connect two permutations if one can be made into the other by swapping two adjacent students. [X]
- B) Vertices represent students. Edges connect two students if they are next to each other in line.
- C) Vertices represent permutations of the students, and each edge represents an individual student. An edge connects two vertices if that student is involved in swap between the two permutations.
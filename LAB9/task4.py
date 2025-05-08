class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value, weight):
        new_node = Node(value, weight)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

class GraphAdjListDirected:
    def __init__(self, size):
        self.size = size + 1
        self.adj = []
        for i in range(self.size):
            self.adj += [LinkedList()]

    def add_edge(self, u, v, weight):
        self.adj[u].insert(v, weight)

    def convert_to_undirected(self):
        new_graph = GraphAdjListDirected(self.size)
        for u in range(self.size):
            current = self.adj[u].head
            while current is not None:
                v = current.value
                w = current.weight
                new_graph.adj[u].insert(v, w)
                new_graph.adj[v].insert(u, w)  
                current = current.next
        return new_graph
    
g1_list = GraphAdjListDirected(7)
g1_list.add_edge(0, 1, 1)
g1_list.add_edge(0, 2, 2)
g1_list.add_edge(0, 3, 5)
g1_list.add_edge(1, 4, 3)
g1_list.add_edge(2, 5, 1)
g1_list.add_edge(5, 7, 3)
g1_list.add_edge(4, 6, 4)
g1_list.add_edge(6, 3, 6)
g1_list.add_edge(7, 3, 7)
new_g = g1_list.convert_to_undirected()
#=======================================================================================================================================================================================
#=======================================================================================================================================================================================
class GraphAdjMatrixDirected:
    def __init__(self, size):
        self.size = size
        self.matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row += [0]
            self.matrix += [row]

    def add_edge(self, u, v, weight):
        self.matrix[u][v] = weight 

    def convert_to_undirected(self):
        new_matrix = GraphAdjMatrixDirected(self.size)
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != 0:
                    new_matrix.matrix[i][j] = self.matrix[i][j]
                    new_matrix.matrix[j][i] = self.matrix[i][j]  
        return new_matrix

g2_matrix = GraphAdjMatrixDirected(7)
g2_matrix.add_edge(0, 1, 1)
g2_matrix.add_edge(0, 2, 2)
g2_matrix.add_edge(0, 3, 5)
g2_matrix.add_edge(1, 4, 3)
g2_matrix.add_edge(2, 5, 1)
g2_matrix.add_edge(4, 6, 4)
g2_matrix.add_edge(6, 3, 6)
g2_matrix.add_edge(7, 3, 7)
g2_matrix.add_edge(5, 7, 3)
new_g = g2_matrix.convert_to_undirected()
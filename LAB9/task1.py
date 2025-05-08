class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def length(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count

class GraphAdjListLinked:
    def __init__(self, vertex_number):
        self.V = vertex_number + 1
        self.Adjacency_list = []
        for i in range(self.V):
            self.Adjacency_list += [LinkedList()]

    def add_edge(self, u, v):
        self.Adjacency_list[u].insert(v)                                                          
        self.Adjacency_list[v].insert(u)  

    def max_degree(self):
        max_deg = 0
        for i in range(self.V):
            deg = self.Adjacency_list[i].length()
            if deg > max_deg:
                max_deg = deg
        return max_deg

# Sample usage for a graph with 7 vertices
g1_list = GraphAdjListLinked(7)
g1_list.add_edge(0, 1)
g1_list.add_edge(0, 2)
g1_list.add_edge(0, 3)
g1_list.add_edge(1, 4)
g1_list.add_edge(2, 5)
g1_list.add_edge(5, 7)
g1_list.add_edge(4, 6)
g1_list.add_edge(6, 3)
g1_list.add_edge(7, 3)
print("Max degree (Adj List):", g1_list.max_degree())


#=======================================================================================================================================================================================
#=======================================================================================================================================================================================


class GraphAdjMatrix:
    def __init__(self, vertex_number):
        self.V = vertex_number + 1

        self.Adjacency_matrix = []
        for i in range(self.V):
            row = []
            for j in range(self.V):
                row += [0]
            self.Adjacency_matrix += [row]
        


    def add_edge(self, u, v):
        self.Adjacency_matrix[u][v] = 1
        self.Adjacency_matrix[v][u] = 1

    def max_degree(self):
        max_deg = 0
        for i in range(self.V):
            count = 0
            for j in range(self.V):
                if self.Adjacency_matrix[i][j] == 1:
                    count += 1
            if count > max_deg:
                max_deg = count
        return max_deg



g2_matrix = GraphAdjMatrix(7)
g2_matrix.add_edge(0, 1)
g2_matrix.add_edge(0, 2)
g2_matrix.add_edge(0, 3)
g2_matrix.add_edge(1, 4)
g2_matrix.add_edge(2, 5)
g2_matrix.add_edge(4, 6)
g2_matrix.add_edge(6, 3)
g2_matrix.add_edge(7, 3)
g2_matrix.add_edge(5, 7)
print("Max degree (Adj Matrix):", g2_matrix.max_degree())

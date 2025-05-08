class Node:
    def __init__(self, elem, weight = None):
        self.elem = elem
        self.next = None
        self.weight = weight

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, elem, weight):
        new_node = Node(elem,weight)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            

    def weightCalc(self):
        weight = 0
        curr = self.head
        while curr is not None:
            weight+= curr.weight
            curr = curr.next
        return weight


class GraphAdjListLinked:
    def __init__(self, vertex_number):
        self.V = vertex_number + 1
        self.Adjacency_list = []
        for i in range(self.V):
            self.Adjacency_list += [LinkedList()]

    def add_edge(self, u, v, weight):
        self.Adjacency_list[u].insert(v, weight)                                                          
        self.Adjacency_list[v].insert(u, weight)

    def vertex_with_max_sum_edge_weight(self):
        max = 0 
        max_vertex = None
        for idx in range(self.V ):
            temp = self.Adjacency_list[idx].weightCalc()
            if temp > max:
                max = temp
                max_vertex = idx
        return max_vertex
    
# Sample usage for a graph with 7 vertices
g1_list = GraphAdjListLinked(7)
g1_list.add_edge(0, 1, 1)
g1_list.add_edge(0, 2, 2)
g1_list.add_edge(0, 3, 5)
g1_list.add_edge(1, 4, 3)
g1_list.add_edge(2, 5, 1)
g1_list.add_edge(5, 7, 3)
g1_list.add_edge(4, 6, 4)
g1_list.add_edge(6, 3, 6)
g1_list.add_edge(7, 3, 7)
print("vertex with Max weight (Adj List):", g1_list.vertex_with_max_sum_edge_weight())

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
        


    def add_edge(self, u, v, weight):
        self.Adjacency_matrix[u][v] = weight
        self.Adjacency_matrix[v][u] = weight

    def vertex_with_max_sum_edge_weight(self):
        max = 0 
        max_vertex = 0
        for i in range(self.V):
            temp = 0
            for j in range(self.V):
                temp += self.Adjacency_matrix[i][j]    
            if temp > max:
                max = temp
                max_vertex = i
        return max_vertex


g2_matrix = GraphAdjMatrix(7)
g2_matrix.add_edge(0, 1, 1)
g2_matrix.add_edge(0, 2, 2)
g2_matrix.add_edge(0, 3, 5)
g2_matrix.add_edge(1, 4, 3)
g2_matrix.add_edge(2, 5, 1)
g2_matrix.add_edge(4, 6, 4)
g2_matrix.add_edge(6, 3, 6)
g2_matrix.add_edge(7, 3, 7)
g2_matrix.add_edge(5, 7, 3)
print("vertex with Max weight (Adj Matrix):", g2_matrix.vertex_with_max_sum_edge_weight())

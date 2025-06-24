class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() \
            and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list[v2] \
            and v2 in self.adj_list[v1]:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        vertices = tuple(self.adj_list[vertex])
        for v1 in vertices:
            result = self.remove_edge(vertex, v1)
            if result == False:
                return result
        del self.adj_list[vertex]
        return result
        
        
if __name__ == "__main__":
    # my_graph = Graph()
    # my_graph.add_vertex('A')
    # my_graph.print_graph()


    # my_graph.add_vertex(1)

    # my_graph.add_vertex(2)

    # my_graph.add_edge(1,2)

    # my_graph.print_graph()

    # my_graph.add_vertex('A')
    # my_graph.add_vertex('B')
    # my_graph.add_vertex('C')

    # my_graph.add_edge('A','B')
    # my_graph.add_edge('B','C')
    # # my_graph.add_edge('C','A')

    # print('Graph before remove_edge():')
    # my_graph.print_graph()


    # my_graph.remove_edge('A','C')


    # print('\nGraph after remove_edge():')
    # my_graph.print_graph()

    my_graph = Graph()
    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')
    my_graph.add_vertex('D')

    my_graph.add_edge('A','B')
    my_graph.add_edge('A','C')
    my_graph.add_edge('A','D')
    my_graph.add_edge('B','D')
    my_graph.add_edge('C','D')


    print('Graph before remove_vertex():')
    my_graph.print_graph()


    my_graph.remove_vertex('D')


    print('\nGraph after remove_vertex():')
    my_graph.print_graph()


from linked_list import SinglyLinkedList
from abc import ABCMeta, abstractmethod

class Graph:
    __metaclass__ = ABCMeta
    num_vertices = 0
    num_edges = 0
    min_degree = 0
    max_degree = 0
    avg_degree = 0
    mediana = 0

    @abstractmethod
    def add_node(self, v1, v2): pass

    def __init__(self, input_path):
        input_file = open(input_path, "r")
        num_vertices = input_file.readline()
        for line in input_file:
            read_string = input_file.readline()
            relation_list = read_string.split(" ")
            add_node(relation_list[0],relation_list[1])
            num_edges += 1
        # Each edge was count twice, so:
        num_edges = num_edges / 2 
 
    def generate_analisys(self, output_path):
        output_file = open(input_path, "w")
        output_file.write(f"Results of the {year} {event}")

class GraphList(Graph):
    adjacency_list = []
    
    def __init__(self, input_path):
        super.__init__(input_path)

        for x in range(0, num_vertices):
            adjacency_list[x] = SinglyLinkedList()
            num_vertices =+ 1
            if adjacency_list[x].num_itens > max_degree:
                max_degree = adjacency_list[x].num_itens
            elif adjacency_list[x].num_itens < min_degree
                min_degree = adjacency_list.num_itens
        avg_degree = num_edges / num_vertices


    def add_node(self, v1, v2):
        adjacency_list[v1].append(v2)

class GraphMatrix(Graph):
    def add_node(self):
        return "Miauuu!"

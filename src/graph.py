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

    @abstractmethod
    def _initialize_data_str(self): pass

    def __init__(self, input_path):
        input_file = open(input_path, "r")
        self.num_vertices = int(input_file.readline())
        print(self.num_vertices)
        self._initialize_data_str()
        for line in input_file:
            read_string = line
            relation_list = read_string.split(" ")
            self.add_node(int(relation_list[0]),int(relation_list[1]))
            self.num_edges += 1
 
    def generate_analisys(self, output_path):
        output_file = open(output_path, "w")
        output_file.write(f"Total vertices: {self.num_vertices}\n")
        output_file.write(f"Total edges: {self.num_edges}\n")
        output_file.write(f"Max degree: {self.max_degree}\n")
        output_file.write(f"Min degree: {self.min_degree}\n")
        output_file.write(f"Avg degree: {self.avg_degree}\n")

class GraphList(Graph):
    adjacency_list = []
    
    def __init__(self, input_path):
        super().__init__(input_path)

    def _initialize_data_str(self):
        print(self.num_vertices)
        for _ in range(0, self.num_vertices):
            self.adjacency_list.append(SinglyLinkedList())

    def add_node(self, v1, v2):
        self.adjacency_list[v1].append(v2)
        
        if self.adjacency_list[v1].num_itens > self.max_degree:
            self.max_degree = self.adjacency_list[v1].num_itens
        elif self.adjacency_list[v1].num_itens < self.min_degree:
            self.min_degree = self.adjacency_list[v1].num_itens
        self.avg_degree = self.num_edges / self.num_vertices

class GraphMatrix(Graph):
    def add_node(self):
        return "Miauuu!"

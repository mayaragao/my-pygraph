from linked_list import SinglyLinkedList
from abc import ABCMeta, abstractmethod
import numpy as np
import queue

class Graph:
    __metaclass__ = ABCMeta
    num_vertices = 0
    num_edges = 0
    min_degree = 0
    max_degree = 0
    avg_degree = 0
    median = 0

    @abstractmethod
    def add_node(self, v1, v2): pass

    @abstractmethod
    def _initialize_data_str(self): pass

    @abstractmethod
    def _set_min_max_degree(self): pass
    
    @abstractmethod
    def bfs(self, root): pass

    def _set_avg_degree(self):
        self.avg_degree = self.num_edges / self.num_vertices

    def __init__(self, input_path):
        input_file = open(input_path, "r")
        self.num_vertices = int(input_file.readline())
        self._initialize_data_str()
        for line in input_file:
            relation_list = line.split(" ")
            self.add_node(int(relation_list[0])-1,int(relation_list[1])-1)
            self.add_node(int(relation_list[1])-1,int(relation_list[0])-1)
            self.num_edges += 1
    
    def generate_analisys(self, output_path):
        self._set_min_max_degree()
        self._set_avg_degree()
        output_file = open(output_path, "w")
        output_file.write(f"Total vertices: {self.num_vertices}\n")
        output_file.write(f"Total edges: {self.num_edges}\n")
        output_file.write(f"Max degree: {self.max_degree}\n")
        output_file.write(f"Min degree: {self.min_degree}\n")
        output_file.write(f"Avg degree: {self.avg_degree}\n")
        output_file.write(f"Median: {self.median}\n")

class GraphList(Graph):
    adjacency_list = []
    
    def __init__(self, input_path):
        super().__init__(input_path)

    def _initialize_data_str(self):
        for _ in range(0, self.num_vertices):
            self.adjacency_list.append(SinglyLinkedList())

    def _set_min_max_degree(self):
        degrees_list = []
        self.min_degree = self.num_vertices
        self.max_degree = 0
        for element in self.adjacency_list:
            degrees_list.append(element.num_itens)
            if element.num_itens < self.min_degree:
                self.min_degree = element.num_itens
            if element.num_itens > self.max_degree:
                self.max_degree = element.num_itens

        degrees_list.sort()
        count = len(degrees_list)

        if count % 2 == 0:
            self.median = (degrees_list[count/2] + degrees_list[(count/2)+1])/2
        else:
            self.median = degrees_list[int(count/2)+1]
        

    def add_node(self, v1, v2):
        self.adjacency_list[v1].append(v2)
        
        if self.adjacency_list[v1].num_itens > self.max_degree:
            self.max_degree = self.adjacency_list[v1].num_itens
    
    def bfs(self, root):
        root = root-1
        level_array = []
        tag_array = []
        parent_array = []

        q = queue.Queue()
       
        # 0 para não descoberto
        # 1 para descoberto
        # 2 para explorado

        for _ in range(0, self.num_vertices):
            tag_array.append(0)
            parent_array.append(0)
            level_array.append(0)

        q.put_nowait(root)
        level_array [root] = 0

        while not q.empty():
            vertex = q.get_nowait()
            for neighbour_str in self.adjacency_list[vertex].get_list():
                neighbour = int(neighbour_str)
                if tag_array[neighbour] == 0:
                    q.put_nowait(neighbour)
                    parent_array[neighbour] = vertex
                    level_array[neighbour] = level_array[neighbour] + 1
                    tag_array[neighbour] = 1
            tag_array[vertex] = 2
            print (f"{vertex+1} {parent_array[vertex]+1} {level_array[vertex]+1}\n")

class GraphMatrix(Graph):
    
    def __init__(self, input_path):
        super().__init__(input_path)

    def add_node(self, v1, v2):
        self.matrix[v1][v2] = True    

    def _initialize_data_str(self):
        self.matrix = np.zeros((self.num_vertices,self.num_vertices), dtype = 'bool')

    def _set_min_max_degree(self):
        self.min_degree = self.num_vertices
        self.max_degree = 0
        for column in self.matrix:
            column_degree = 0
            for line in column:
                if line == True:
                    column_degree += 1
            if column_degree < self.min_degree:
                self.min_degree = column_degree
            if column_degree > self.max_degree:
                self.max_degree = column_degree


    def bfs(self, root):
        root = root-1
        level_array = []
        tag_array = []
        parent_array = []

        q = queue.Queue()
       
        # 0 para não descoberto
        # 1 para descoberto
        # 2 para explorado

        for _ in range(0, self.num_vertices):
            tag_array.append(0)
            parent_array.append(0)
            level_array.append(0)

        q.put_nowait(root)
        level_array [root] = 0

        while not q.empty():
            vertex = q.get_nowait()
            for i, element in enumerate(self.matrix[vertex]):
                if element == True:
                    if tag_array[i] == 0:
                        q.put_nowait(i)
                        parent_array[i] = vertex
                        level_array[i] = level_array[i] + 1
                        tag_array[i] = 1
            tag_array[vertex] = 2
            print (f"{vertex+1} {parent_array[vertex]+1} {level_array[vertex]+1}")
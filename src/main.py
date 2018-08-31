from graph import GraphList

def main():
    graph = GraphList("../examples/as_graph.txt")
    print(graph.num_vertices)
    graph.generate_analisys("../output/as_graph_out.txt")

main()

    
    

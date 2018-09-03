from graph import *

def main():
    graph = GraphList("../examples/teste.txt")
    graph.generate_analisys("../output/as_graph2.txt")
    graph.bfs(1)

main()

    
    

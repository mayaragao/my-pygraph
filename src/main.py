from graph import *
import time
import random

def main():
    print("Loading graph...")
    graph = GraphList("../examples/dblp.txt")
    print("Loaded!")
    array = []
    
    for i in range(0,10):
        start_time = time.time()
        graph.bfs(random.randint(1,graph.num_vertices))
        print(i)
        now = time.time() - start_time
        array.append(now)
        print(now)

    sum = 0
    for x in array:
        sum += x

    media = sum/len(array)

    print(f"Tempo médio {media}s!!")
    


main()

    
    

INF=9999
def floydAlgo(graph):
    print("Original Matrix")
    showMatrix(graph)
    n=len(graph)
    for k in range(n): 
        for i in range(n): 
            for j in range(n): 
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) 
        print("After Step",k+1,"Matrix A: ")
        showMatrix(graph)

def showMatrix(matrix):
    n=len(graph)
    for i in range(n): 
        for j in range(n):
            if (matrix[i][j]==INF):
                print(u"\u221E", end = "\t")
                #print('INF', end = "\t")
            else:
                print(matrix[i][j], end = "\t") 
        print()
        
graph = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floydAlgo(graph)

#method 2
# import numpy as np
# def floydWarshall(graph):
#     dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
#     for k in range(V):
#         for i in range(V):
#             for j in range(V):
#                 dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
#     printSolution(dist)
# def printSolution(dist):
#     print("The shortest distances are : ")
#     for i in range(V):
#         for j in range(V):
#             if(dist[i][j] == INF):
#                  print("%7s" % ("∞"),end =" ")
#             else:
#                 print("%7d" % (dist[i][j]),end= " ")
#             if j == V-1:
#                 print("")
# V = 4
# INF = np.inf
# graph = np.array([[0, 3, INF, 7],
#          [3, 0, 2, INF],
#          [3, INF, 0, 1],
#          [2, INF, INF, 0]])
# floydWarshall(graph)

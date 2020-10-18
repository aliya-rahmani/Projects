V=4
INF=999

def Floyd_Warshall(graph):
    distance = list(map(lambda i: list(map(lambda j: j, i)),graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distance[i][j] = min(distance[i][j], (distance[i][k] + distance[k][j]))
    print_solution(distance)


def print_solution(distance):
    for i in range(V):
        for j in range(V):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


graph=[[0,3,INF,5],
       [2,0,INF,4],
       [INF,1,0,INF],
       [INF,INF,2,0]]

Floyd_Warshall(graph)

        

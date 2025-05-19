# Function to find BFS of Graph from given source s
def bfs(adj):
    
    # inisiasi vektor (output matriks)
    V = len(adj) #inputan jumlah vertex
    
    # inisiasi list untuk menyimpan hasil BFS
    res = []
    s = 0

    # buat queue untuk BFS
    from collections import deque
    q = deque()
    
    # Initially mark all the vertices as not visited
    visited = [False] * V
    
    # Mark source node as visited and enqueue it
    visited[s] = True
    q.append(s)
    
    # Iterate over the queue
    while q:
        
        # Dequeue a vertex from queue and store it
        curr = q.popleft()
        res.append(curr)
        
        # Get all adjacent vertices of the dequeued 
        # vertex curr If an adjacent has not been 
        # visited, mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
                
    return res

if __name__ == "__main__":
    
    # create the adjacency list
    # [ [2, 3, 1], [0], [0, 4], [0], [2] ]
    adj = [[1,2], [0,1,3], [0,4], [2,4], [1,3,4]]
    ans = bfs(adj)
    for i in ans:
        print(i, end=" ")
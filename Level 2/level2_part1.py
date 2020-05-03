import Queue as queue

def solution(src, dest):
    if src == dest:
        return 0
    
    h = src/8
    g = src % 8
        
        
    q = queue.Queue()
    knight_p = [-2 , -2 , -1 , -1 , 1 , 2 , 2 , 1]
    knight_q = [1 , -1 , 2 , -2 , -2 , -1 , 1 , 2]

    visited = [[False for i in range(8)]  
                      for j in range(8)] 
    
    q.put((h,g,0))
    visited[h][g] = True
    while(q.empty() == False):
        a = q.get()

        if ((a[0]*8) + a[1]) == dest:
            return a[2] 

        for i in range(8):
            new_x = a[0] + knight_p[i]
            new_y = a[1] + knight_q[i]
            
            if(new_x>=0 and new_x<8 and new_y>=0 and new_y<8 ):
                if(visited[new_x][new_y] == False):
                    q.put((new_x,new_y,a[2]+1))
                    visited[new_x][new_y] = True

    return 0        

moves = solution(0,1)
print(moves)

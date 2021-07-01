def get_next(m, x, y):
    for next_y in range(y+1, 9):
        if m[x][next_y] == 0:
            return x, next_y
    for next_x in range(x+1, 9): 
        for next_y in range(0, 9):
            if m[next_x][next_y] == 0:
                return next_x, next_y
    return -1, -1 
        
def value(m, x, y):
    i, j = x//3, y//3
    grid = [m[i*3+r][j*3+c] for r in range(3) for c in range(3)]
    v = set([x for x in range(1,10)]) - set(grid) - set(m[x]) - \
        set(list(zip(*m))[y])    
    return v

def start_pos(m):
    for x in range(9):
        for y in range(9):
            if m[x][y] == 0:
                return x, y
    return -1, -1

def try_sudoku(m, x, y):   
    for v in value(m, x, y):
        if m[x][y] == 0:  
            m[x][y] = v
            next_x, next_y = get_next(m, x, y)            
            if next_y == -1: 
                print(m)
                return True
            else:
                end = try_sudoku(m, next_x, next_y) 
                if end:
                    return True
                m[x][y] = 0   

def sudoku(m):        
    x, y = start_pos(m)
    for v in value(m, x, y):        
        m[x][y] = v
        next_x, next_y = get_next(m, x, y)
        try_sudoku(m, next_x, next_y)
             
                    
if __name__ == "__main__":
    m = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    sudoku(m)

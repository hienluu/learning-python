from collections import deque
import queue

# array grid list[list[int]] where 0 is empty cell and 1 is wall

def bfs(grid:list[list[int]], start_row:int, start_col:int) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    visited = {(start_row, start_col)} # of tuples (row, col)

    # initiailize distance grid with -1 for unvisited cells
    distance_grid = [[-1] * cols for _ in range(rows)]
    distance_grid[start_row][start_col] = 0

    # initialize queue with starting position and distance 0
    queue = deque([(start_row, start_col, 0)]) # (row, col, distance)

    while queue:
        row, col, dist = queue.popleft()
        # explore in all four neighboring directions
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)): #down, up, right, left
            # for each neighborb
            nr, nc = dr + row, dc + col
            # check if the neighbord is with bounds
            # haven't visisted it yet
            # and is not a wall
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
                distance_grid[nr][nc] = dist + 1
    return distance_grid

def bfs2(grid: list[list[int]], start_row:int, start_col: int) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    visited = {(start_row, start_col)}

    dist_grid = [[-1] * cols for _ in range(rows)]
    dist_grid[start_row][start_col]= 0

    queue = deque([(start_row, start_col, 0)]) # row, col, dist
    while queue:   	    
        row, col, dist = queue.popleft()
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = dr + row, dc + col
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
                dist_grid[nr][nc] = dist + 1
    return dist_grid
       

    
  

if __name__ == "__main__":
    grid = [
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    start_row = 0
    start_col = 0
    result = bfs(grid, start_row, start_col)
    for row in result:
        print(row)

    print("**** bfs2 result: *****")
    result2 = bfs2(grid, start_row, start_col)
    for row in result2:
        print(row)
    #print(f"result: {bfs(grid, start_row, start_col)}")
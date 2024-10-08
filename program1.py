class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    
    def dfs(r, c):
      
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or (r, c) in visited:
            return
      
        visited.add((r, c))
      
        dfs(r + 1, c)  
        dfs(r - 1, c)  
        dfs(r, c + 1)  
        dfs(r, c - 1)  

    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'L' and (r, c) not in visited:
                
                dfs(r, c)
                island_count += 1  

    return island_count


dispatch_1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"],
]

dispatch_2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"],
]

print(getTotalIsles(dispatch_1))  
print(getTotalIsles(dispatch_2))  


        

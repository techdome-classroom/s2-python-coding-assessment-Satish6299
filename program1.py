def numIslands(grid):
    if not grid:
        return 0
    
    def dfs(grid, i, j):
        # Check for bounds and whether the current cell is land ("L")
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return
        # Mark this land as visited by converting it to water ("W")
        grid[i][j] = 'W'
        # Traverse all four directions (up, down, left, right)
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)
    
    num_islands = 0
    
    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':  # Found an unvisited land
                dfs(grid, i, j)   # Perform DFS to mark the entire island
                num_islands += 1  # Increment the island count
    
    return num_islands

# Example Test Cases:

# Dispatch 1
grid1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"],
]
print(numIslands(grid1))  # Output: 1

# Dispatch 2
grid2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"],
]
print(numIslands(grid2))  # Output: 3

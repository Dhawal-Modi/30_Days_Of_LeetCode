class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if(grid == None or len(grid) == 0):
            return 0
        
        count = 0
        
        #Two nested for loops for travesing input grid
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == '1':
                    count += self.dfs(grid,i,j)
        return count
    
    #Implement a dfs approach to traverse and apply the island condition on the grid
    def dfs(self,grid,i,j):
        
        #Check for boundary conditions while travesing the 2D grid
        if (i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=='0'):
            return 0
        
        #Set visited islands to '0' so that we do not visit them again
        grid[i][j] = '0'
        
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        return 1

class Solution:
    
    def flyod_warshall(self, mat):

        n = len(mat)

        for i in range(n):
            for j in range(n):
                if mat[i][j] == -1:
                    mat[i][j] = float('inf')
                if i == j:
                    mat[i][j] = 0
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][via] != float('inf') and mat[via][j] != float('inf'):
                        mat[i][j] = min(mat[i][j], mat[i][via] + mat[via][j])
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] == float('inf'):
                    mat[i][j] = -1
        
        for i in range(n):
            if mat[i][i] < 0:
                return "negative cycle found"
        
        return mat


# Example usage
matrix = [
    [0, 3, -1, 7],
    [-1, 0, 2, -1],
    [-1, -1, 0, 1],
    [6, -1, -1, 0]
]

print(matrix)
solution = Solution()
result = solution.flyod_warshall(matrix)
print(result)
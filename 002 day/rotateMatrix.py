class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ln=len(mat)
        
        # transpose
        for i in range(ln-1):
            for j in range(i+1,ln):
                mat[i][j],mat[j][i]= mat[j][i],mat[i][j]
                
        for j in range(ln):
            l,r=0,ln-1
            while l<r:
                mat[j][l],mat[j][r]=mat[j][r],mat[j][l]
                l+=1
                r-=1
class Solution:
    def searchMatrix(self, matrix, target):
        start,end  = 0,len(matrix)-1
        while start<=end:
            row = (start+end)//2
            if target > matrix[row][-1]:
                start = row+1
            elif target < matrix[row][0]:
                end = row-1
            else:
                break
        if not(start<=end):
            return False
        row = (start+end)//2
        start,end = 0,len(matrix[row])-1
        while start<=end:
            mid = (start+end)//2
            if target> matrix[row][mid]:
                start = mid+1
            elif target<matrix[row][mid]:
                end = mid-1
            else:
                return True
        return False
z=Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
print(z.searchMatrix(matrix,target))


class Solution:
    def search(self, nums, target):
        l=0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target > nums[m]:
                l=m+1
            elif target < nums[m]:
                r=m-1
            else:
                return m
        return -1
z=Solution()
nums = [-1,0,3,5,9,12]
target =13
print(z.search(nums,target))
class Solution:
    def findMin(self, nums):
        min_num = nums[0]
        l = 0
        r = len(nums)-1
        while l<=r:
            if nums[l]<nums[r]:
                min_num = min(min_num,nums[l]) 
                break
            m=(l+r)//2
            if nums[m]>=nums[l]:
                l = m+1
            else:
                r=m-1
        return min_num


nums = [3,4,5,1,2]
z=Solution()
print(z.findMin(nums))
        
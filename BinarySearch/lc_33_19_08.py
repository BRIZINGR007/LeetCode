class Solution:
    def search(self, nums, target) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[m]>=nums[l]:
                if target>nums[m] or target<nums[l]:#3678012 t=0
                    l=m+1
                else:#3678012 t = 6
                    r=m-1
            else:#nums[m]<nums[l]
                if target<nums[m] or target > nums[r]:
                    r=m-1
                else:
                    l=m+1



        return -1
nums = [4,5,6,7,0,1,2]
target = 0
z=Solution()
print(z.search(nums,target))
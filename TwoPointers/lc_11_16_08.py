class Solution:
    def maxArea(self, height):
        l,r = 0,len(height)-1
        curr_area=0
        max_area=0
        while l<r:
            curr_area=min(height[l],height[r])*(r-l)
            max_area = max(curr_area,max_area)
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                l+=1
                r-=1
        return max_area


z=Solution()
print(z.maxArea(height = [1,8,6,2,5,4,8,3,7]))

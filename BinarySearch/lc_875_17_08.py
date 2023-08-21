import math
class Solution:
    def minEatingSpeed(self, piles, h):
     l,r=1,max(piles)
     res = r
     while l<=r:
          mid = (l+r)//2
          for i in piles:
               hours += math.ceil(i/mid)
          if hours <= h:
               res = min(res,mid)
               l=mid+1
          else:
               r = mid-1
     return res
          
     

          
piles = [3,6,7,11]
h = 8
z = Solution()
print(z.minEatingSpeed(piles,h))
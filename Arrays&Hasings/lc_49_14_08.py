import collections
class Solution:
    def groupAnagrams(self, strs):
        res = collections.defaultdict(list)
        for i in strs:
            count = [0]*26
            for n in i:
                count[ord(n)-ord('a')]+=1
            res[tuple(count)].append(i)
        return res.values()
   
z=Solution()
print(z.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

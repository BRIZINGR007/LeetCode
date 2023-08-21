class Solution:
    def characterReplacement(self, s: str, k: int):
        l=0
        hashmap={}
        max_len = 0
        for r in range(len(s)):
            hashmap[s[r]]=1+hashmap.get(s[r],0)
            if (r+1-l) - max(hashmap.values())<=k:
                max_len=max((r+1-l),max_len)
            else:
                hashmap[s[l]]-=1
                l+=1
                
        return max_len

s = "ABAA"
k = 0
z=Solution()
print(z.characterReplacement(s,k))
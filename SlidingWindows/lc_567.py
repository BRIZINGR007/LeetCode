class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1Count={}
        s2Count={}
        for i in range(len(s1)):
            s1Count[s1[i]]=1+s1Count.get(s1[i],0)
            s2Count[s2[i]]=1+s2Count.get(s2[i],0)
        matches = 0
        for i in range(len(s1Count)):
            matches+=(1 if s1Count[s1[i]]==s2Count[s2[i]] else 0)
        
        l=0
        for i in range(len(s1Count),len(s2Count)):
            if matches==len(s1Count):return True
            s2Count[s2[i]]+=1
            if s1Count[s1[i]]==s2Count[s2[i]] 
        


s1 = "ab"
s2 = "eidbaooo"
z=Solution()
print(z.checkInclusion(s1,s2))
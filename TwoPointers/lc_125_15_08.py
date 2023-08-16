class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        l = len(s)-1
        while f<=l:
            if not s[f].isalnum():
                f+=1
            elif not s[l].isalnum():
                l-=1
            elif s[f].lower()==s[l].lower():
                f+=1
                l-=1
            elif s[f].lower() != s[l].lower():
                return False
        return True
z =Solution()
s = "A man, a plan, a canal: Panama"
print(z.isPalindrome(s))
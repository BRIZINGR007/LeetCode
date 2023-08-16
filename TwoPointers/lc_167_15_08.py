class Solution:
    def twoSum(self, numbers, target):
        hashmap=[]
        for i in range(len(numbers)):
            if numbers[i] in hashmap:
                return (hashmap.index(numbers[i])+1,i+1)
            k = target - numbers[i]
            hashmap.append(k)
            





numbers = [2,7,11,15]
target = 9
z= Solution()
print(z.twoSum(numbers,target))

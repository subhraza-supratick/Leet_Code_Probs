class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        length=len(nums)
        appear=length//2
        i=0
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for j in hashmap:
            if hashmap[j]>appear:
                return j


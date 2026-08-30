class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        window_sum=0
        largest_sum=0
        count={}
        while right<len(nums):
            window_sum+=nums[right]
            if nums[right] in count:
                count[nums[right]]+=1
            else:
                count[nums[right]]=1
            window_size=right-left+1
            if window_size==k:
                if len(count)==k:
                    if window_sum>largest_sum:
                        largest_sum=window_sum
                window_sum-=nums[left]
                
                count[nums[left]]-=1
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1
                
            right+=1
            
        return largest_sum



    
        
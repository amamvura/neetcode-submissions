class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            j = target - nums[i]

            if j in h and h[j] != i:
                return [i, h[j]]

                
            
        
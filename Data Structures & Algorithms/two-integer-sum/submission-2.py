class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fast = 1
        slow = 0

        while slow < len(nums):
            
            while fast < len(nums):
                
                if nums[slow] + nums[fast] == target:
                    return [slow,fast]
                fast+=1
            slow+=1
            fast = slow+1

        return []
            

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for x in range(len(nums)):
            if mp.get(nums[x]) != None:
                return True
            else:
                mp[nums[x]] = 1
        return False
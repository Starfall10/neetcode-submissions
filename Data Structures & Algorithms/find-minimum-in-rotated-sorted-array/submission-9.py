class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        m = nums[0]
        while left <= right:
            mid = (left+right) // 2
            print(mid)
            print("left", left, "right", right)
            curr = nums[mid]
            print("curr", curr, "m", m)
            if curr >= m:
                left = mid + 1
            else:
                if nums[mid-1] < curr:
                    right = mid -1
                else:
                    return curr

            

            


                
        return m
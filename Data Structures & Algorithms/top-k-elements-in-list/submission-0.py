class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}


        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1
                
        # 2. Create buckets
        # index = frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # 3. Put numbers into frequency buckets
        for num, count in mp.items():
            freq[count].append(num)

        # 4. Traverse from highest frequency to lowest
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
        

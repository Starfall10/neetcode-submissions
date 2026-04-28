class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}

        for c in s:
            if c not in mp:
                mp[c] = 1
            else:
                mp[c] +=1
        
        for c in t:
            if c not in mp:
                return False
            else:
                mp [c] -=1
                if mp[c] == 0:
                    mp.pop(c, None)
        if len(mp) != 0:
            return False
        return True
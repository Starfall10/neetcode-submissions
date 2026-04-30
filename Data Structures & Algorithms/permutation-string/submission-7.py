class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # m = {}
        # n = len(s1)

        # for c in s1:
        #     if c in m:
        #         m[c] +=1
        #     else:
        #         m[c] = 1
        
        # print(m)
        # print(len(s2)-n)
        # for i in range(0, len(s2)-n+1):

        #     curr = s2[i:i+n]
        #     print(curr)
        #     copym = m.copy()
        #     print(copym)
        #     b = True

        #     for c in curr:
        #         if c in copym:
        #             copym[c] -= 1
        #             if copym[c] == 0:
        #                 copym.pop(c, None)
        #         else:
        #             b = False
        #             break
            
        #     if b:
        #         return True

        # return False


        if len(s1) > len(s2):
            return False

        s1map = defaultdict(int)

        for c in s1:
            s1map[c] += 1
        
        n = len(s1)
        m = len(s2)
        s2map = defaultdict(int)

        for i in range(n):
            s2map[s2[i]] += 1
        
        if s1map == s2map:
            return True
        
        s2map[s2[0]] -= 1
        if s2map[s2[0]] == 0:
            s2map.pop(s2[0])
        
        l = 1

        for r in range(n, m):
            s2map[s2[r]] += 1

            if s2map == s1map:
                return True

            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                s2map.pop(s2[l])

            l += 1

        return False

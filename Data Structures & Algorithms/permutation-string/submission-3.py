class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = {}
        n = len(s1)

        for c in s1:
            if c in m:
                m[c] +=1
            else:
                m[c] = 1
        
        print(m)
        print(len(s2)-n)
        for i in range(0, len(s2)-n+1):

            curr = s2[i:i+n]
            print(curr)
            copym = m.copy()
            print(copym)
            b = True

            for c in curr:
                if c in copym:
                    copym[c] -= 1
                    if copym[c] == 0:
                        copym.pop(c, None)
                else:
                    b = False
                    break
            
            if b:
                return True

        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*128
        b = [0]*128
        for i in s:
            a[ord(i)] += 1
        
        for i in t:
            b[ord(i)] += 1

        return a == b
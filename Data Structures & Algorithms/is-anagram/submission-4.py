class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*27
        for i in s:
            a[ord(i)-97] += 1
        
        for i in t:
            a[ord(i)-97] -= 1

        return a == [0]*27
class Solution:
    def countingSortString(self, s: str) -> str:
        cnt = [0]*26

        for i in s:
            cnt[ord(i)-97] += 1
        
        return "".join(chr(i+97)*cnt[i] for i in range(len(cnt)))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = 0
        d = dict()
        ans = list()

        for s in strs:
            S = self.countingSortString(s)
            if S not in d:
                ans.append([s])
                d[S] = cnt
                cnt += 1
            else:
                ans[d[S]].append(s)

        return ans
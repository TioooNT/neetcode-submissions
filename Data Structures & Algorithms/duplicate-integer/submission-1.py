class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        S = set()

        for i in nums:
            if i in S:
                return True
            
            S.add(i)
        
        return False

        
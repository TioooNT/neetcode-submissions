class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict()

        for i, c in enumerate(nums):
            if target-c in d:
                return [d.get(target-c), i]
            d[c] = i
        

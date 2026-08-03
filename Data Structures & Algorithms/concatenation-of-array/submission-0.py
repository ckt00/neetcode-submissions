class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums.copy()
        return ans
    
        
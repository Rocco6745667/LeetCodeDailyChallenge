class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        lb = bisect_left(nums, 0)
        ub = bisect_right(nums, 0)
        
        return max(lb, n - ub)
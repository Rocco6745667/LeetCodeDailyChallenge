class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        ans = mx = 0

        for j, i in enumerate(values):
            ans = max(ans, mx + i - j)
            mx = max(mx, i + j)

        return ans
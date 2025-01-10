class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        ans = 0
        
        for i, j in enumerate(words):
            for t in words[i + 1:]:
                ans += t.endswith(j) and t.startswith(j)
        
        return ans
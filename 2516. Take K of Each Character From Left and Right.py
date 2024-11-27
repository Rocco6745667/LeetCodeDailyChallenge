class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        count = Counter(s)
        
        if any(count[c] < k for c in "abc"):
            return -1

        mx = j = 0

        for i, c in enumerate(s):
            
            count[c] -= 1
            
            while count[c] < k:
                count[s[j]] += 1
                j += 1
            
            mx = max(mx, i - j + 1)
        
        return len(s) - mx

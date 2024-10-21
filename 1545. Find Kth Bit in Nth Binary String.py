class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S = ['0']
#function to invert and reverse the list representing string for n
        def transform(L): 
            for i in range(len(L)):
                if L[i] == "0":
                    L[i] = "1"
                else:
                    L[i] = "0"
            return L[::-1]
# Now generate list for each n starting from 2 to n
        for i in range(2, n+1):
            S = S + ['1'] + transform(S)
        return S[k-1]
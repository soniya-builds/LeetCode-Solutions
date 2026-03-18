class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
        return -1
    
    
sol = Solution()

print(sol.strStr("sadbutsad", "sad"))   # Expected: 0
print(sol.strStr("leetcode", "leeto"))  # Expected: -1
print(sol.strStr("hello", "ll"))        # Expected: 2
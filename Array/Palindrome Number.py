class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        list2 = list(str(x))     # convert number to list
        copy_list2 = list2.copy()   # make copy
        copy_list2.reverse()        # reverse copy
        
        if list2 == copy_list2:
            return True
        else:
            return False
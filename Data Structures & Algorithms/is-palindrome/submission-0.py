class Solution:
    def isPalindrome(self, s: str) -> bool:
        #copy_s = s.lower()
        #reverse_s = copy_s[::-1]
        #if copy_s == reverse_s:
            #return True
        #return False
        copy_s = ""   
        for char in s:
            if char.isalnum():
                copy_s = copy_s + char.lower()
        reverse_s = copy_s[::-1]
        if copy_s == reverse_s:
            return True
        return False
            
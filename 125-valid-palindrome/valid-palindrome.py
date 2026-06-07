class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        t = "".join(c for c in t if c.isalnum())
        
        if t == t[::-1]:
            return True
        else:
            return False
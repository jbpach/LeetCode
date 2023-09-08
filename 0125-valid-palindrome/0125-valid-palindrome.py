class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = ''.join(c.lower() for c in s if c.isalnum())
    
        start = 0;
        end = len(s) - 1
        
        while start < end:
            if s[start] == s[end]:
                start += 1;
                end -= 1;
            else: 
                return False
        return True
        
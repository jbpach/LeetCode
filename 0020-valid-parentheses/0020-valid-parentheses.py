class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        validPairs = { ')': '(' , '}' : '{' , ']' : '[' }
        stack = []
        for i in range(len(s)):
            if s[i] not in  validPairs: 
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif stack[len(stack) - 1] == validPairs[s[i]]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0        
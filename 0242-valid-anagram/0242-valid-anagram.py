class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dict_s = {}
        dict_t = {}
        
        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
                
        for i in range(len(t)):
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
                
        return dict_s == dict_t
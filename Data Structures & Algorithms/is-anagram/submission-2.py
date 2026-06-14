class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s, t)
        if len(s) != len(t):
            return False

        s_freq = [0] * 26
        t_freq = [0] * 26
        for i in range(len(s)):
            s_freq[ord(s[i])-ord('a')] = s_freq[ord(s[i])-ord('a')] + 1
            t_freq[ord(t[i])-ord('a')] = t_freq[ord(t[i])-ord('a')] + 1
            
        for i in range(26):
            if s_freq[i] != t_freq[i]:
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        for i in s:
            if i in count_s:
                count_s[i] += 1      # add 1, seen before
            else:
                count_s[i] = 1       # first instance, count 1 
        count_t = {} #same thing, diff var
        for i in t:
            if i in count_t:
                count_t[i] += 1
            else:
                count_t[i] = 1
        return count_s == count_t
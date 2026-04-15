class Solution:

    def encode(self, strs):
        return "".join(str(len(s)) + "#" + s for s in strs) # .join to avoid commas
        #for s in strs it makes an ecoding eg for "Hello" it goes "5#Hello" 

    def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result
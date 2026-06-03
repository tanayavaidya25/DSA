class Solution(object):
    def reverseWords(self, s):
        m=s.split()
        m.reverse()

        return " ".join(m)
        
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        rstr, vowel = list(s), list("aeiou")
        vowel_pos = [pos for pos, c in enumerate(s) if c in vowel]
        d = list()
        for e in vowel_pos:
            d.append(e)
            if len(d) == 2:
                t = rstr[d[0]]
                rstr[d[0]] = rstr[d[1]]
                rstr[d[1]] = t
                t = d[-1]
                d = []
                d.append(t)
        return "".join(rstr)

st = Solution()
st.reverseVowels(list("aA"))
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


def lengthOfLongestSubstring(self, s):
    charset = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l += 1
        charset.add(s[r])
        res = max(res, r - l)
    return res
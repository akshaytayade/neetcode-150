# Leetcode premium
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in str:
            res += str(len(s)) + "|" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(i):
            j = i
            while s[j] != "|":
                j += 1
                length = int(s[i:j])
                res.append(s[j+1:j+1+length])
                i = j + 1 + length
        return res

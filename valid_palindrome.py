def valid_palindrome(self, s):
    l, r = 0, len(s) - 1 # initiliaztion of two pointers
    while l < r:
        while l < r and not alphaNum(s[l]): 
            l += 1
        while l < r and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower(): # use lowercase comparison
            return False
        
        l, r = l+1, r-1
        return True

def alphaNum(self, c): ## use ascii values to compare if the given char is a alphanum char or not
    return (
        ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z')
        ord('0') <= ord(c) <= ord('9')
    )
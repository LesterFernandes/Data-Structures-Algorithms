def longestPalindrome(s: str) -> str:
    if len(s) == 0:
        return False
    pal = ''
    i = 0
    while i < len(s):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            substr = s[l: r + 1]
            if len(substr) > len(pal):
                pal = substr
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            substr = s[l: r + 1]
            if len(substr) > len(pal):
                pal = substr
            l -= 1
            r += 1
        i += 1

    return pal

# print(longestPalindrome('zshszi')) --> 'zshsz'
# print(longestPalindrome('momdewednun')) --> 'dewed'

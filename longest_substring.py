def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    l,r = 0,1
    maxlen = 0
    while r < len(s):
        if s[r] not in s[l:r]:
            r += 1
            maxlen = max(maxlen, r-l)
        else:
            l += 1
    return maxlen

print(lengthOfLongestSubstring('asdfg'))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(" "))

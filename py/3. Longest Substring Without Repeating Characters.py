def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    lookup = set()
    max_length = 0
    result = ""
    i, j = 0, 0
    while j < len(s):
        if s[j] not in lookup:
            if max_length < (j - i + 1):
                max_length = j - i + 1                    
                result = s[i:j+1]
            lookup.add(s[j])
            j += 1
        else:
            if s[i] in lookup:
                lookup.remove(s[i])
            i += 1
    return max_length, result

print(lengthOfLongestSubstring("abcdefg"))
print(lengthOfLongestSubstring("abcdefgabcdefg"))
print(lengthOfLongestSubstring("abcdefgabcdefgabcdefg"))
print(lengthOfLongestSubstring("aaaaa"))
print(lengthOfLongestSubstring("bbbbb"))
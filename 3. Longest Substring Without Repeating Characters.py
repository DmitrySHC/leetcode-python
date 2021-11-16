'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s: str) -> int:
    res = right = 0
    my_list = []
    while right < len(s):
        if s[right] not in my_list:
            my_list.append(s[right])
            right += 1
        else:
            if len(my_list) > res:
                res = len(my_list)
            my_list = my_list[my_list.index(s[right])+1:]
    return res if len(my_list) < res else len(my_list)
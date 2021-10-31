'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.
'''


def isValid(s):
    brackets = []
    s_dict = {"(": ")", "{": "}", "[": "]"}
    for char in s:
        if char in s_dict:
            brackets += [s_dict[char]]
        elif len(brackets) == 0 or char != brackets.pop():
            return False
    return not brackets

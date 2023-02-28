"""
Check if the input string is valid all parenthesis must be closed by another one.
"""


def validParenthesis(s):

    if len(s) <= 0:
        return True

    # Define a stack and put first character
    arr = [s[0]]

    for i in range(1, len(s)):
        if s[i] == '}':
            if s[i-1] == '{':
                arr.pop()
            else:
                arr.append(s[i])
        elif s[i] == ')':
            if s[i-1] == '(':
                arr.pop()
            else:
                arr.append(s[i])
        elif s[i] == ']':
            if s[i-1] == '[':
                arr.pop()
            else:
                arr.append(s[i])
        else:
            arr.append(s[i])

        print(arr)

    return len(arr) == 0


print(validParenthesis("{{[]}}"))

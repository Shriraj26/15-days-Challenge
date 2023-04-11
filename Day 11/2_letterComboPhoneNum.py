
def letterCombo(digits):

    if len(digits) == 0:
        return ''

    phoneNo = ''
    newArr = []

    # building a string with no zeros and ones
    for i in digits:
        if i != '0' and i != '1':
            phoneNo += i

    buff = [None] * len(phoneNo)

    myDict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def genCombo(strIndex, buffIndex):

        # if u go out of buffer
        if buffIndex == len(buff):
            print(buff)
            return

        # if u go out of string index
        if strIndex == len(phoneNo):
            return

        for i in range(strIndex, len(phoneNo)):

            for char in myDict[phoneNo[i]]:
                buff[buffIndex] = char
                genCombo(i+1, buffIndex + 1)

    genCombo(0, 0)


letterCombo('456')

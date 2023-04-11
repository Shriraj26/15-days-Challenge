"""
Go through it one time...
"""


class Stack:
    def __init__(self):
        self.stack = []

    def peek(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)
        return True

    def size(self):
        return len(self.stack)

    def print(self):
        print(self.stack)


class Solution:
    def calculate(self, s: str) -> int:
        self.operand = Stack()
        self.operator = Stack()
        self.chars = []

        for index, char in enumerate(s):
            if index != 0 and s[index-1].isdigit() and s[index].isdigit():
                self.chars[-1] = str(int(self.chars[-1])*10 + int(char))
            else:
                self.chars.append(char)

        for (index, char) in enumerate(self.chars):
            if char.isdigit():
                self.operand.push(int(char))
            elif char in ("+", "-", "/", "*"):
                while self.operator.size() > 0 and self.precedence(self.operator.peek()) >= self.precedence(char):
                    # self.operator.print()
                    # self.operand.print()
                    # print(char)
                    self.process()
                    # self.operator.print()
                    # self.operand.print()
                self.operator.push(char)
            elif char == "(":
                self.operator.push(char)
            else:
                while self.operator.peek() != "(":
                    self.process()
                self.operator.pop()

        while self.operator.size() > 0:
            self.process()
        # self.operand.print()
        # self.operator.print()
        return self.operand.pop()

    def process(self):
        operand1 = self.operand.pop()
        operand2 = self.operand.pop()

        operator = self.operator.pop()
        if operator == "+":
            self.operand.push(operand1 + operand2)
        elif operator == "-":
            self.operand.push(operand2-operand1)
        elif operator == "*":
            self.operand.push(operand2*operand1)
        elif operator == "/":
            if operand2//operand1 < 0:
                self.operand.push(operand2//operand1+1)
            else:
                self.operand.push(operand2//operand1)

        return

    def precedence(self, op):
        map = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "(": 0
        }

        if op not in map:
            return 0
        return map[op]

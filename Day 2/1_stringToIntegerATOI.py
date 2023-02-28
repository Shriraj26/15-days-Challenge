"""
We use Finite State Machines to solve this type of problem.
Use this link for more details...
https://towardsdatascience.com/using-state-machine-to-solve-complex-coding-interview-questions-2b8897e23582
This is a very good example to solve problems using finite state machine where
we define a diagram in which the machine moves from one state to another and does the job.
"""


def atoi(s):

    def inRange(num):
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if num < -2 ** 31:
            return -2 ** 31
        return num

    states = {
        1: {'blank': 1, 'sign': 2, 'integer': 3},
        2: {'integer': 3},
        3: {'integer': 3},
    }

    currentState = 1
    sign = 1
    value = 0
    stateDef = ''

    for i in s:

        # Define the stateDef
        if i == ' ':
            stateDef = 'blank'
        elif i in '0123456789':
            stateDef = 'integer'
        elif i in '+-':
            stateDef = 'sign'
        else:
            stateDef = 'else'

        # break the loop if stateDef is not within the current State in dict
        if stateDef not in states[currentState]:
            break

        # Process the number
        if stateDef == 'sign':
            sign = 1 if i == '+' else -1
        elif stateDef == 'integer':
            value = value * 10 + int(i)

        # move to the next state
        currentState = states[currentState][stateDef]

    return inRange(sign * value)


print(atoi('words forever'))

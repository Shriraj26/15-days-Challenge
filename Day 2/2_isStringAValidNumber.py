"""
This is also an example to solve a problem using fsm..
Refer to this link - https://towardsdatascience.com/using-state-machine-to-solve-complex-coding-interview-questions-2b8897e23582
The diagram is a bit complex but you will get the transition
from one state to another
"""


def isStringValidNumber(s):

    states = {

        # No state
        0: {},

        # Init state, u can go to digit, sign, or dot from this state
        1: {'blank': 1, 'sign': 2, 'digit': 3, 'dot': 4},

        # Sign state, u can go to digit or dot from this state
        2: {'digit': 3, 'dot': 4},

        # Digit state, u can towards self, or through dot to after dot , or through e to found e, or end
        3: {'digit': 3, 'dot': 5, 'e': 6, 'blank': 9},

        # Dot state, u can go to after dot state from this state
        4: {'digit': 5},

        # After Dot state
        5: {'digit': 5, 'e': 6, 'blank': 9},

        # Found e
        6: {'digit': 8, 'sign': 7},

        # Sign After e,
        7: {'digit': 8},

        # Digit After e
        8: {'blank': 9, 'digit': 8},

        # last state
        9: {'blank': 9}
    }

    currentState = 1

    for i in s:

        stateDef = None
        # Define the stateDef
        if i in '0123456789':
            stateDef = 'digit'
        elif i in '+-':
            stateDef = 'sign'
        elif i == '.':
            stateDef = 'dot'
        elif i == 'e':
            stateDef = 'e'
        elif i == ' ':
            stateDef = 'blank'
        else:
            stateDef = 'else'

        # break from loop if no matching state found
        if stateDef not in states[currentState]:
            return False

        # Shift to the next state
        currentState = states[currentState][stateDef]

    return currentState in [3, 5, 8, 9]

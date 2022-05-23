# DSA2 Assignment
# Graph Algorithms on DFAs

from random import *

from dfa import DFA


# region Question 1

def createDFA():
    # creating required variables
    symbols = ['a', 'b']
    states = randint(16, 24)
    transitions = {}

    #
    for cnt in range(0, states):
        state1 = randint(0, states - 1)
        state2 = randint(0, states - 1)

        transitions[cnt] = {'a': state1, 'b': state2}

    # using sample() and random to choose a random number to be accepting or not accepting
    accepting = sample(transitions.keys(), k=(round(0.2 * states)))

    # choosing a random state as the starting state of the DFA
    startingState = randint(0, states - 1)

    # getting states that are not accepting

    allStates = [cnt for cnt in range(0, states)]
    notAccepting = list(set(allStates).symmetric_difference(accepting))

    return DFA(states, accepting, notAccepting, symbols, startingState, transitions)

# endregion


def main():
    newDFA = createDFA()

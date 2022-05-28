# DSA2 Assignment
# Graph Algorithms on DFAs
# Luke D'Amato

from dfa import DFA

from random import *


# region Question 1
def createDFA():
    # creating variable states and giving it a random value 16-24
    states = randint(16, 24)

    transitions = {}  # creating a dict signifying the transitions of this particular DFA
    symbols = ['a', 'b']  # creating a list with 2 possible symbols 'a' and 'b', as required

    # creating random transitions by iterating through each state
    for cnt in range(0, states):
        state1 = randint(0, states - 1)
        state2 = randint(0, states - 1)

        transitions[cnt] = {'a': state1, 'b': state2}

    # using sample() and random to choose a random number to be accepting or not accepting
    startingState = randint(0, states - 1)  # choosing a random state as the starting state of the DFA
    accepting = sample(transitions.keys(), k=(round(0.2 * states)))

    # getting states that are not accepting
    allStates = [cnt for cnt in range(0, states)]
    notAccepting = list(set(allStates).symmetric_difference(accepting))

    print("========== Question1 ==========")
    print("The DFA has been created")

    return DFA(states, accepting, notAccepting, symbols, startingState, transitions)

# endregion


def main():
    # Question 1
    dfa = createDFA()

    # Question 2
    print("\n========== Question 2 ==========")
    print('Current automaton: A')
    dfa.getDepth()

    # Question 3
    dfa.minimize()

    # Question 4
    print("\n========== Question 4 ==========")
    print('Current automaton: M')
    dfa.getDepth()

    # Question 5
    dfa.checkDFA()
    dfa.getSCC()

    # Question 6


main()

# DSA2 Assignment
# Graph Algorithms on DFAs
# Luke D'Amato

import random


# region static method for question 3
def findStates(transitions, x, A):
    stateFound = []

    # looping through the values found in transitions
    for state, values in transitions.items():

        if (x in values.keys()) and (values[x] in A):
            # if x is found in values and element x is found in M, append
            # current state to the states found list
            stateFound.append(state)

    return stateFound
# endregion


class DFA:

    # initialising an init function for the creating of the DFA
    def __init__(self, states, accepting, rejecting, symbol, starting, transition):
        # creating variable in self for the number of states (a)
        self.states = states
        # determining whether the state is accepting or not (b)
        self.accepting = accepting
        self.rejecting = rejecting
        # creating transition variable for the random states and for the symbols (c)
        self.symbol = symbol
        self.transition = transition
        # choosing a random state for starting state (d)
        self.starting = starting

    # region Question 2

    # As suggested, implementing the breadth-first search to eventually get the depth
    def breadthFirstSearch(self, starting):

        queue = [starting]  # a list to check states and their children
        history = [starting]  # a list with the states that have been searched

        # creating a dict to store the depths of each node from the starting state
        nodeDepth = {cnt: 0 for cnt in range(self.states)}

        while len(queue) != 0:
            currentNode = queue[0]
            queue.pop(0)  # removing the first element

            for nodes, currValue in self.transition[currentNode].items():

                #  checking whether the nodes where visited or not
                if currValue not in history:
                    history.append(currValue)
                    queue.append(currValue)

                    nodeDepth[currValue] = nodeDepth[currValue] + 1

        # Getting the max depth as well as the states of that depth, and returning them
        maxDepth = max(nodeDepth.values())
        maxes = [cnt for cnt, depth in nodeDepth.items() if depth == maxDepth]

        return maxes, maxDepth

    # creating a function to get the Depth of the required Automaton
    def getDepth(self):
        maxes, maxDepth = self.breadthFirstSearch(self.starting)
        # storing max depth node
        maxNode, finalDepth = maxes, maxDepth

        # using a for loop to find the max distance and updating the maxDepth
        for states in maxes:
            # calculating the node with the longest path from the prev. node using temp vars
            tempMax, tempDepth = self.breadthFirstSearch(states)

            if tempDepth > finalDepth:
                maxNode = tempMax
                finalDepth = tempDepth

        if self.states and finalDepth:
            # Printing the number of states and depth as required
            print("number of states in 'current automaton': ", self.states)
            print("depth of 'current automaton': ", finalDepth)
        else:
            print("Error - one or both of the values is empty")
        return finalDepth

    # endregion

    # region Question 3
    # For this question, I have decided to got with Hopcroft minimization
    # algorithm in order to create the new Automaton M

    # function to find the states in the Automaton that reach M from a character x
    def findTransitions(self, A, partitions):
        # using a dict to store the new transitions
        newTransitions = {}
        oldTransitions = self.transition[A]

        # looping for each character in the symbol
        for x in self.symbol:

            if x in oldTransitions.keys():
                state = oldTransitions[x]

                # looping through each partition in the current symbol
                for cnt, partition in enumerate(partitions):

                    if state in partition:
                        newTransitions[x] = cnt
                        break
        return newTransitions

    def hopcroftMinAlg(self):
        # while dist (distinguishers) only have accepting states
        dist = [self.accepting]
        # partitions need to include both accepting and rejecting states
        partitions = [self.accepting, self.rejecting]

        # loops until length of dist is not 0
        while len(dist) != 0:
            A = dist.pop(0)

            # iterating through all the DFA symbols
            for i in self.symbol:
                X = findStates(self.transition, i, A)

                # iterating through all the partitions in the partition using enumerate and a temp counter
                for j, subPartition in enumerate(partitions[:]):
                    inter = list(set(X).intersection(subPartition))
                    diff = list(set(subPartition).difference(X))

                    # checking that both intersection and difference are not empty
                    if len(inter) != 0 and len(diff) != 0:
                        partitions.remove(subPartition)
                        partitions.append(inter)
                        partitions.append(diff)

                        # check if partition is found in distinguishers
                        if subPartition in dist:
                            dist.remove(subPartition)
                            dist.append(inter)
                            dist.append(diff)
                        else:
                            if len(inter) <= len(diff):
                                dist.append(inter)
                            else:
                                dist.append(diff)

        return partitions

    def minimize(self):
        partitions = self.hopcroftMinAlg()

        # creating dict and lists to store new data after minimization
        newTransitions = {}
        newAccepting = []
        newRejecting = []
        newStart = self.starting

        # looping through each partition in partitions while keeping count (cnt)
        for cnt, partition in enumerate(partitions):

            # checking partitions for a starting node
            if self.starting in partition:
                newStart = cnt

            A = partition[0]

            # checking whether the current partition is accepting or not
            if A in self.accepting:
                newAccepting.append(cnt)
            else:
                newRejecting.append(cnt)

            newTransitions[cnt] = self.findTransitions(A, partitions)

        self.states = len(partitions)
        self.transition = newTransitions
        self.starting = newStart
        self.accepting = newAccepting
        self.rejecting = newRejecting

        # checking to make sure none of the values is empty
        if len(partitions) != 0 and newTransitions and newStart and newAccepting and newRejecting:
            print("\n========== Question 3 ==========")
            print("Successfully minimized automaton A and created automaton M")
        else:
            print("Error - One of the values is empty")

    # endregion

    # region Question 4

    # for this question, we are using the same function getDepth() we used in Question 2

    # endregion

    # region Question 5
    def checkDFA(self):
        numString = 100
        lenString = 128

        print("\n========== Question 5 ==========")

        # using a for loop to iterate through the number of strings (numString) or through new strings
        for i in range(numString):
            currentState = self.starting
            currString = ''

            # generating a random character each iteration through a random number (0-lenString)
            for j in range(0, random.randint(0, lenString)):
                chars = random.choice(self.symbol)
                # adding the random char to the current string
                currString += chars

                if chars not in self.transition[currentState]:
                    currentState = None
                    break
                # setting transition to the next state with the given character
                currentState = self.transition[currentState][chars]

                # ** used for testing **
                # if currentState in self.accepting:
                #     print("Current string: " + currString + " is accepting")
                # else:
                #     print("Current string: " + currString + " is rejecting")

    # implementing Tarjan's algorithm using Depth First Search (DFS)
    def tarjanDFS(self, currState, inStack, SCCstates, lowLink, stack):

        # assigning and ID and low link value to the current State
        SCCstates[currState] = self.SCCstate
        lowLink[currState] = self.SCCstate

        self.SCCstate += 1

        # setting the value on stack as true with the current state as element of the list
        inStack[currState] = True
        # finally, appending the current State to the stack
        stack.append(currState)

        # using a for loop to iterate through the neighbours of the current
        # State using the childNode as the element
        for childNode in self.transition[currState].values():
            if SCCstates[childNode] == -1:
                self.tarjanDFS(childNode, inStack, SCCstates, lowLink, stack)

            if inStack[childNode]:
                lowLink[currState] = min(lowLink[childNode], lowLink[currState])

        if lowLink[currState] == SCCstates[currState]:
            currSCC = []
            current = -1

            while current != currState:
                current = stack.pop()  # popping the stack in the current position
                inStack[current] = False  # setting the stack element as False
                currSCC.append(current)  # finally, appending the current SCC

            self.SCC.append(currSCC)  # appending final value to the self

    # Creating required variables to keep track
    SCC = []
    SCCstate = 0

    # creating the function in order to get components that are seperated
    def getSCC(self):
        self.SCCstate = 0
        self.SCC = []

        lowLinkVals = [-1] * self.states  # storing all low link values
        trackStack = []  # keeping track of all the checked states
        SCCstates = [-1] * self.states  # a list that contains the IDs of the discovered state

        inStack = [False] * self.states  # keeping track of all the states in the stack

        for cnt in range(self.states):

            # get SDD if state is not yet found
            if SCCstates[cnt] == -1:
                self.tarjanDFS(cnt, inStack, SCCstates, lowLinkVals, trackStack)

        numOfSCCs = len(self.SCC)
        largestSCC = max(self.SCC, key=len)
        smallestSCC = min(self.SCC, key=len)

        # used for testing
        # print(self.SCC)
        # print(largestSCC)
        # print(smallestSCC)

        if largestSCC and smallestSCC:
            print("number of strongly connected components in M: ", numOfSCCs)
            print("size of (number of states in) the largest SCC in M: ", len(largestSCC))
            print("size of (number of states in) the smallest SCC in M: ", len(smallestSCC))
        else:
            print("Error - lists are empty")

    # endregion

    # region Question 6

    # endregion

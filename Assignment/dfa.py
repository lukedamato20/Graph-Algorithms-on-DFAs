# DSA2 Assignment
# Graph Algorithms on DFAs

import random


class DFA:

    # initialising an init function for the creating of the DFA
    def __init__(self, states, accepting, rejecting, symbol, starting, transition):
        self.states = states  #
        self.accepting = accepting  #
        self.rejecting = rejecting  #
        self.symbol = symbol  #
        self.starting = starting  #
        self.transition = transition  #

    # region Question 2

    def breadthFirstSearch(self, starting):

        queue = [starting]  # a list to check states and their children
        history = [starting]  # a list with the states that have been searched

        # creating a dict to store the depths of each node from the starting state
        nodeDepth = {cnt: 0 for cnt in range(self.states)}

        while len(queue) != 0:
            currentNode = queue[0]
            queue.pop(0)  # removing the first element

            for nodes, currValue in self.transition[currentNode].nodes():
                #  checking whether the nodes where visited or not
                if currValue not in history:
                    history.append(currValue)
                    queue.append(currValue)

                    nodeDepth[currValue] = nodeDepth[currValue] + 1

        # Getting the max depth as well as the states of that depth, and returning them
        maxDepth = max(nodeDepth.values())
        maxes = [cnt for cnt, depth in nodeDepth.items() if depth == maxDepth]

        return maxDepth, maxes

    # creating a function to get the Depth of the required Automaton
    def getDepth(self):
        maxes, maxDepth = self.breadthFirstSearch(self.starting)
        # storing max depth node
        maxNode = maxes
        finalDepth = maxDepth

        # using a for loop to find the max distance and updating the maxDepth
        for states in maxes:
            # calculating the node with the longest path from the prev. node using temp vars
            tempMax, tempDepth = self.breadthFirstSearch(states)

            if tempDepth > tempMax:
                maxNode = tempMax
                finalDepth = tempDepth

        # Printing the number of states and depth as required
        print("Number of states in A: ", self.states)
        print("Depth of A: ", finalDepth)
        return finalDepth

    # endregion

    # region Question 3

    # function to find the states in the Automaton that reach M from a character x
    def findStates(self, transitions, x, A):
        stateFound = []
        # looping through the values found in transitions
        for state, values in transitions.items():
            if (x in values.keys()) and (values[x] in A):
                # if x is found in values and element x is found in M, append current state to the states found list
                stateFound.append(state)

        return stateFound

    def findTransitions(self, A, partitions):
        transitions = self.transition[A]
        # using a dict to store the new transitions
        newTransitions = {}
        # looping for each character in the symbol
        for x in self.symbol:
            if x in transitions.keys():
                state = transitions[x]
                # looping through each partition in the current symbol
                for cnt, partitions in enumerate(partitions):
                    if state in partitions:
                        newTransitions[x] = cnt
                        break
        return newTransitions

    def hopcroftMinAlg(self):
        # partitions need to include both accepting and rejecting states
        partitions = [self.accepting, self.rejecting]
        # while dist (distinguishes) only have accepting states
        dist = [self.accepting]

        # loops until length of dist is not 0
        while len(dist) != 0:
            A = dist.pop(0)

            for i in self.symbol:
                X = self.findStates(self.transition, i, A)

                for j, partition in enumerate(partitions[:]):
                    inter = list(set(X).intersection(partition))
                    diff = list(set(partition).difference(X))
                    # checking that both intersection and difference are not empty
                    if len(inter) != 0 and len(diff) != 0:
                        partitions.remove(partition)
                        partitions.append(inter)
                        partitions.append(diff)

                        # check if partition is found in distinguisher
                        if partition in dist:
                            dist.remove(partition)
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
        newStart = []
        newAccepting = []
        newRejecting = self.starting

        # looping through all the partitions while keeping count (cnt)
        for cnt, partitions in enumerate(partitions):
            # checking partitions for a starting node
            if self.starting in partitions:
                newStart = cnt

            A = partitions[0]

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
    # endregion

    # region Question 4

    # for this question, we are using the same function getDepth() we used in Question 2

    # endregion

    # region Question 5

    # endregion

    # region Question 6

    # endregion


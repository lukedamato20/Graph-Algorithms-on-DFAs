# Graph-Algorithms-on-DFAs
ICS2210 - Data Structures and Algorithms 2, Course Project 2022

Construct a deterministic finite state automaton A according to the following
recipe:
  Create n states, where n is a random number between 16 and 64 inclusive.
  For each state, flip a coin to determine whether the state is accepting or not.
  Every one of the n states must have two outgoing transitions leading to two other random states; 
    one transition is labelled with the symbol a, and the other with the symbol b. Transitions from a state to itself (loops) are allowed.
  Choose any random state as the starting state of the DFA.

Compute the depth A! of A. The depth of an automaton is defined as the maximum over all states of the length of the 
shortest string which leads to that state (hint: you can use breadth-first search to get this).

  Print the number of states in A.
  Print the depth A! of A.

Minimise the automaton A using either the Moore or Hopcroft minimization algorithm to obtain a new automaton M.

Compute the depth M" of M.
  Print the number of states in M.
  Print the depth M" of M.

Learn what strongly connected components (SCCs) in graphs are and implement Tarjan’s algorithm for finding the strongly connected components in M.
  Print the number of strongly connected components in M.
  Print the size of (number of states in) the largest SCC in M.
  Print the size of (number of states in) the smallest SCC in M.

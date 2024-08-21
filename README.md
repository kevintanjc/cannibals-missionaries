# cannibals-missionaries

# Problem Statement
Given m missionaries, c cannibals and a boat of size 2, how do i get all the people from the right side of a river over to the left side of the river

# My Solution
Model the puzzle as a Tree Problem, with nodes representing the puzzle state and edges between two nodes representing a legal move.

A move is legal if the cannibals do not kill any missionaries.

# Restrictions
1. m, c has to be greater than 0
2. size of c has to be at most size m

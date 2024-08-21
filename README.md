# Spies & Target Puzzle 🔪

# Problem Statement
Given m Spies, c Targets and a Car of size 2, how do i get all the people from Town R over to Town L without the spies killing any targets?

Spies will assassinate Targets if there are more Spies than Targets in either Towns.

# My Solution
Model the puzzle as a Tree Problem, with nodes representing the puzzle state and edges between two nodes representing a legal move.

A move is legal if the spies do not kill any targets in any Town.

# Restrictions
1. m, c has to be greater than 0
2. size of c has to be at most size m

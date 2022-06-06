# AI_tic_tac_toe

AI that given a state of a classic (3x3) tic tac toe board can return an optimal move 

Input: 
A path to a file with the following format:
	- the first line will contain either X or O depending on which player should make the next move
	- the following 3 lines will contain one line of the board each, with None marking free spaces

Example input file:
X
None None O
X X O
None None None

Output:
the script outputs the x and y coordinate for the optimal move (indexed from 0) or -1, -1 if the input is invalid
# **********************
# Picobot empty maze
# **********************

# state 0 goes N as far as possible
0 **x* -> W 0   # if there's nothing to the N, go N
0 **Wx -> S 0   # if N is blocked, switch to state 1
0 **WS -> X 1

# state 1 goes right
1 *x** -> E 1   # Go right
1 *E** -> N 2   # Hit right wall, change to state 2

# state 2 goes left
2 **x* -> W 2  # Go left 
2 **W* -> N 1  # If hit left wall, change to state 1

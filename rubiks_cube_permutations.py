from sympy.combinatorics.permutations import Permutation

# Define permutations using array notation (0-indexed)
# SymPy indexes from 0, so we put 0 to nonexistent 0-cubicle 
# so it doesn't effect or calculations or notation in our paper

# Cubicle Permutations (disregards cube orientation within cubicle)
R = Permutation(2,6,7,3)
U = Permutation(1,2,4,3)
L = Permutation(1,4,8,5)
D = Permutation(8,7,6,5)
B = Permutation(2,1,5,6)
R_inv = ~R
U_inv = ~U
L_inv = ~L
D_inv = ~D
B_inv = ~B


# Facelet Permutations: Using Jamie Mulholand's notation (https://www.sfu.ca/~jtmulhol/math302/puzzles-rc-representation.html)
# Rf = Permutation([0,1,19,3,17,5,6,7,8,9,2,11,4,14,16,15,13,24,18,22,20,21,10,23,12])
# Uf = Permutation([0,2,4,1,3,17,18,7,8,5,6,11,12,9,10,15,16,13,14,19,20,21,22,23,24])
# Lf = Permutation([0,9,2,11,4,6,8,5,7,21,10,23,12,13,14,15,16,17,3,19,1,20,22,18,24])
# Df_inv = Permutation([0,1,2,3,4,5,6,19,20,9,10,7,8,13,14,11,12,17,18,15,16,23,21,24,22]) #Accidentally found D'!

Rf = Permutation(13,14,16,15)(10,2,19,22)(12,4,17,24)
Uf = Permutation(1,2,4,3)(9,5,17,13)(10,6,18,14)
Lf = Permutation(5,6,8,7)(3,11,23,18)(1,9,21,20)
Df = Permutation(21,22,24,23)(11,15,19,7)(12,16,20,8)
Bf = Permutation(17,18,20,19)(1,7,24,14)(2,5,23,16)

Rf_inv = ~Rf
Uf_inv = ~Uf
Lf_inv = ~Lf
Df_inv = ~Df




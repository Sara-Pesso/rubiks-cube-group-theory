from sympy.combinatorics.permutations import Permutation

# Define permutations using array notation (0-indexed)
# SymPy indexes from 0, so we put 0 to nonexistent 0-cubicle 
# so it doesn't effect or calculations or notation in our paper

# Cubicle Permutations (disregards cube orientation within cubicle)
R = Permutation(2,6,7,3)
U = Permutation(1,2,3,4)
L = Permutation(1,4,8,5)
D = Permutation(8,7,6,5)
B = Permutation(2,1,5,6)
F = Permutation(3,7,8,4)

R_inv = ~R
U_inv = ~U
L_inv = ~L
D_inv = ~D
B_inv = ~B
F_inv = ~F


# Facelet Permutations: Using Jamie Mulholand's notation (https://www.sfu.ca/~jtmulhol/math302/puzzles-rc-representation.html)

Rf = Permutation(13,14,16,15)(10,2,19,22)(12,4,17,24)
Uf = Permutation(1,2,4,3)(9,5,17,13)(10,6,18,14)
Lf = Permutation(5,6,8,7)(3,11,23,18)(1,9,21,20)
Df = Permutation(21,22,24,23)(11,15,19,7)(12,16,20,8)
Bf = Permutation(17,18,20,19)(1,7,24,14)(2,5,23,16)
Ff = Permutation(9,10,12,11)(3,13,22,8)(4,15,21,6)

Rf_inv = ~Rf
Uf_inv = ~Uf
Lf_inv = ~Lf
Df_inv = ~Df
Ff_inv = ~Ff




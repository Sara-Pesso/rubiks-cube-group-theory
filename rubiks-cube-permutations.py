from sympy.combinatorics.permutations import Permutation

# Define permutations using array notation (0-indexed)
# SymPy indexes from 0, so we put 0 to nonexistent 0-cubicle 
# so it doesn't effect or calculations or notation in our paper

# Cubicle Permutations (disregards cube orientation within cubicle)
R = Permutation([0,1,6,2,4,5,7,3,8]) 
U = Permutation([0,2,3,4,1,5,6,7,8])
L = Permutation([0,4,2,3,8,1,6,7,5])
D_inv = Permutation([0,1,2,3,4,6,7,8,5]) #Accidentally found D'!
R_inv = ~R
U_inv = ~U
L_inv = ~L
D = ~D_inv

# Facelet Permutations: Using Jamie Mulholand's notation (https://www.sfu.ca/~jtmulhol/math302/puzzles-rc-representation.html)
Rf = Permutation([0,1,19,3,17,5,6,7,8,9,2,11,4,14,16,13,15,24,18,22,20,21,10,23,12])
Uf = Permutation([0,2,4,1,3,17,18,7,8,5,6,11,12,9,10,15,16,13,14,19,20,21,22,23,24])
Lf = Permutation([0,9,2,11,4,6,8,5,7,21,10,23,12,13,14,15,16,17,3,19,1,20,22,18,24])
Df_inv = Permutation([0,1,2,3,4,5,6,19,20,9,10,7,8,13,14,11,12,17,18,15,16,23,21,24,22]) #Accidentally found D'!
Rf_inv = ~Rf
Uf_inv = ~Uf
Lf_inv = ~Lf
Df = ~Df_inv

# Group Theory Operations!
# Commutator RUR'U'
commutator = R*U*R_inv*U_inv
print("Commutator: [R,U] = RUR'U'")
print("Cubicle notation:")
print(f"Commutator: {commutator}")             # Permutation multiplication
print(f"Order: {commutator.order()}")          # Order of the permutation
print(f"Cycle Form: {commutator.cyclic_form}") # Cycle notation
print(f"Permutation Form: {commutator.array_form}") # Permutaion notation
print(f"Sign: {commutator.signature()}")       # Sign of permutation

print("Facelet notation:")
commutator = Rf*Uf*Rf_inv*Uf_inv
print(f"Commutator: {commutator}")             # Permutation multiplication
print(f"Order: {commutator.order()}")          # Order of the permutation
print(f"Cycle Form: {commutator.cyclic_form}") # Cycle notation
print(f"Permutation Form: {commutator.array_form}") # Permutaion notation
print(f"Sign: {commutator.signature()}")       # Sign of permutation


# Commutator [R, U ′L′U ] = RU ′L′U R′U ′LU
commutator = R*U_inv*L_inv*U*R_inv*U_inv*L*U
print("Commutator: [R, U'L'U ] = RU'L'UR'U'LU")
print("Cubicle notation:")
print(f"Commutator: {commutator}")             # Permutation multiplication
print(f"Order: {commutator.order()}")          # Order of the permutation
print(f"Cycle Form: {commutator.cyclic_form}") # Cycle notation
print(f"Permutation Form: {commutator.array_form}") # Permutaion notation
print(f"Sign: {commutator.signature()}")       # Sign of permutation

print("Facelet notation:")
commutator = Rf*Uf_inv*Lf_inv*Uf*Rf_inv*Uf_inv*Lf*Uf
print(f"Commutator: {commutator}")             # Permutation multiplication
print(f"Order: {commutator.order()}")          # Order of the permutation
print(f"Cycle Form: {commutator.cyclic_form}") # Cycle notation
print(f"Permutation Form: {commutator.array_form}") # Permutaion notation
print(f"Sign: {commutator.signature()}")       # Sign of permutation

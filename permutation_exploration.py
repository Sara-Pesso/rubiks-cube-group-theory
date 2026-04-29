from rubiks_cube_permutations import *
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
print(f"Simple Transpositions: {commutator.transpositions()}")
print(f"Sign: {commutator.signature()}")       # Sign of permutation

print("Facelet notation:")
commutator = Rf*Uf_inv*Lf_inv*Uf*Rf_inv*Uf_inv*Lf*Uf
print(f"Commutator: {commutator}")             # Permutation multiplication
print(f"Order: {commutator.order()}")          # Order of the permutation
print(f"Cycle Form: {commutator.cyclic_form}") # Cycle notation
print(f"Permutation Form: {commutator.array_form}") # Permutaion notation
print(f"Simple Transpositions: {commutator.transpositions()}")
print(f"Sign: {commutator.signature()}")       # Sign of permutation


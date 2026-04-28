from rubiks_cube_permutations import *

# Luckily we only R,U,L, and D for this algorithm which saves me a ton of time!

S = R*U # Initial Scrambled Configuration: Solved Configuration * R * U
S_ = Rf*Uf
print(f"Inital State: {S.array_form}")


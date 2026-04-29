from rubiks_cube_permutations import *
from collections import Counter

# Luckily we only R,U,L, and D for this algorithm which saves me a ton of time!

# Initial Scrambled Configuration: Solved Configuration * R * U
Sf = Rf*Uf
#The inverse will give us the current configuration of the Pcket Cube at each step!
print(f"Inital State (Facelets): {(~Sf).array_form}")


#Algorithm
# 0. In 3-D, the solved position can be rotated and still be solved. 
# Here, we're confinded to one specific configuration. So, we are basically
# solving the top layer, but on the bottom. That means the facelets we are considered with 
# will map like this:
# Facelet 1 in Position 21
# Facelet 2 in Position 22
# Facelet 3 in Position 23
# Facelet 4 in Position 24
#This will solve the white face, which is label as face U on my Pocket Cube!

moves_performed = []

# If facelet 1 is on Down face, pass
if (~Sf).array_form[21] == 1 or (~Sf).array_form[22] == 1 or (~Sf).array_form[23] == 1 or (~Sf).array_form[24] == 1:
    pass

# If on Up face,
elif (~Sf).array_form[1] == 1 or (~Sf).array_form[3] == 1:
    Sf = Sf*Lf*Lf
    moves_performed.append('L')
    moves_performed.append('L')
elif (~Sf).array_form[2] == 1 or (~Sf).array_form[4] == 1:
    Sf = Sf*Rf*Rf
    moves_performed.append('R')
    moves_performed.append('R')

# If on Left face,
elif (~Sf).array_form[5] == 1:
    Sf = Sf*Uf*Rf
    moves_performed.append('U')
    moves_performed.append('R')
elif (~Sf).array_form[6] == 1:
    Sf = Sf*Uf*Lf
    moves_performed.append(U)
    moves_performed.append('L')
elif (~Sf).array_form[7] == 1:
    Sf = Sf*Df*Rf
    moves_performed.append('D')
    moves_performed.append('R')
elif (~Sf).array_form[8] == 1:
    Sf = Sf*Df*Lf
    moves_performed.append('D')
    moves_performed.append('L')

# If on Front face,
elif (~Sf).array_form[9] == 1 or (~Sf).array_form[11] == 1:
    Sf = Sf*Lf
    moves_performed.append('L')
elif (~Sf).array_form[10] == 1 or (~Sf).array_form[12] == 1:
    Sf = Sf*Rf_inv
    moves_performed.append(R_inv)

# If on Right face, 
elif (~Sf).array_form[13] == 1:
    Sf = Sf*Uf*Lf
    moves_performed.append('U')
    moves_performed.append('L')
elif (~Sf).array_form[14] == 1:
    Sf = Sf*Uf*Rf
    moves_performed.append('U')
    moves_performed.append('R')
elif (~Sf).array_form[15] == 1:
    Sf = Sf*Df*Lf
    moves_performed.append('D')
    moves_performed.append('L')
elif (~Sf).array_form[16] == 1:
    Sf = Sf*Df*Rf
    moves_performed.append('D')
    moves_performed.append('R')

# If on Back face, 
elif (~Sf).array_form[17] == 1 or (~Sf).array_form[19] == 1:
    Sf = Sf*Rf
    moves_performed.append('R')
elif (~Sf).array_form[18] == 1 or (~Sf).array_form[20] == 1:
    Sf = Sf*Lf_inv
    moves_performed.append('L_inv')

# Once on Down face, rotate using D until facelet 1 is in position 21:
while (~Sf).array_form[21] != 1:
    Sf = Sf*Df
    moves_performed.append('D')


# SOLVE THE TOP LAYER (WHITE) ON THE BOTTOM FACE!
if (~Sf).array_form[21] == 1: #Position 21 (i.e., Facelet 1 in position 21) can be hard coded 
                            # because it is constant
    
    facelet_order = [2,4,3] # Moving to positions: [22,24,23]
    for i in range(0, len(facelet_order)):
        facelet = facelet_order[i]

        # If facelet is already correctly positioned, skip to next 
        if (~Sf).array_form[22] == facelet:
            Sf = Sf*Df_inv
            moves_performed.append('D_inv')
            break 
        
        # 1. Regardless of orientation, find the cube we need to move into cubicle 7,
        # and perform U until it is in cubicle 3.
        
        # If cubie we need is on top layer, rotate it in to cubicle 3
        if facelet in [(~Sf).array_form[i] for i in [1,2,3,4,5,6,9,10,13,14,17,18]]: # all top layer facelets
            while facelet not in [(~Sf).array_form[i] for i in [4,10,13]]: #Cubicle 3
                Sf= Sf*Uf
                moves_performed.append('U')
        elif facelet in [(~Sf).array_form[i] for i in [7,20,23]]: # Cubicle 5
            Sf = Sf*Bf*Bf*Rf_inv
            moves_performed.append('B')
            moves_performed.append('B')
            moves_performed.append('R_inv')
        else: # Cubicle 6 or 7
            pass
            #TODO
            
        #2 . Repeat the following commutator until the cube in cubicle 3, is oriented
        # correctly in cubicle 7:
        # [R, U ] = RUR'U'
        # Order of facelets placed: [22,24,23]
        # Cube 8, Facelet 21 is already correctly positioned
        
        while (~Sf).array_form[22] != facelet:
            #Apply commutator
            Sf = Sf*Rf*Uf*Rf_inv*Uf_inv
            moves_performed.extend(['R','U', 'R_inv','U_inv'])

        # 3. Once complete, perform D′.
        Sf = Sf*Df_inv
        moves_performed.append('D_inv')

        # 4. For Loop: Repeat steps 2-3 until the bottom layer is completely solved.
    
    # to get facelet 1 into position 21 again, hit D' once more
    Sf = Sf*Df_inv
    moves_performed.append('D_inv')

    # 5. Looking at the top layer of cubes, see if they are in the correct cubicles,
    # regardless of their orientations. There will either be 1, 2, or 4 cubes in
    # the correct cubicles. If there are 4, skip to step (8). If there are 1 or
    # 2, perform the following commutator, performing U D to get a correctly
    # positioned cube into cubicle 4 (i.e., front left):
    # [R, U ′L′U ] = RU ′L′U R′U ′LU

    #Bools if the remaining cubes are in the correct cubicle:        
    def cubicle_positions():
        cubicles = {1:[1,5,18],
                    2:[2,14,17],
                    3:[4,10,13],
                    4:[3,6,9],
                    5:[7,20,23],
                    6:[16,19,24],
                    7:[12,15,22],
                    8:[8,11,21]}

        
        current_state = (~Sf).array_form
        f1 = [key for key, values in cubicles.items() if current_state.index(1) in values][0]
        f2 = [key for key, values in cubicles.items() if current_state.index(2) in values][0]
        f3 = [key for key, values in cubicles.items() if current_state.index(3) in values][0]
        f4 = [key for key, values in cubicles.items() if current_state.index(4) in values][0]

        f21 = [key for key, values in cubicles.items() if current_state.index(21) in values][0]
        f22 = [key for key, values in cubicles.items() if current_state.index(22) in values][0]
        f23 = [key for key, values in cubicles.items() if current_state.index(23) in values][0]
        f24 = [key for key, values in cubicles.items() if current_state.index(24) in values][0]

        pairs = {f1:f23,
                 f2:f24,
                 f3:f21,
                 f4:f22}
        matches = {8:4,
            7:3,
            6:2,
            5:1}
        
        correct_positions_bool = []
        current_positions = []
        for bottom, top in pairs.items():
           current_positions.append([bottom, top])
           if (bottom, top) in matches.items():
               correct_positions_bool.append(True)
           else:
               correct_positions_bool.append(False) #[f1~f23, f2~f24, f3~f21, f4~f22]

        return correct_positions_bool, current_positions

    correct_positions_bool, current_positions = cubicle_positions()

    # 5. Looking at the top layer of cubes, see if they are in the correct cubicles,
    # regardless of their orientations. There will either be 1, 2, or 4 cubes in
    # the correct cubicles. If there are 4, skip to step (8). If there are 1 or
    # 2, perform the following commutator, performing U D to get a correctly
    # positioned cube into cubicle 4 (i.e., front left):
    # [R, U ′L′U ] = RU ′L′U R′U ′LU

    # 6. Check again, performing U if necessary to get 1 cubicle in the correct
    # position.

    # 7. Repeat steps 5-6 until all 4 cubes are in the correct cubicles, regardless of
    # orientation.

    while sum(correct_positions_bool) != 4:
        match sum(correct_positions_bool):
            case 0:
                Sf = Sf*Uf
                moves_performed.append('U')
                correct_positions_bool, current_positions = cubicle_positions()
            case 1:
                while [8,4] not in [current_positions[i] for i in range(len(correct_positions_bool)) if correct_positions_bool[i]]:
                    Sf = Sf*Uf*Df_inv
                    moves_performed.extend(['U, D_inv'])
                    correct_positions_bool, current_positions = cubicle_positions()

                # Apply commutator
                Sf = Sf*Rf*Uf_inv*Lf_inv*Uf*Rf_inv*Uf_inv*Lf*Uf
                moves_performed.extend(['R, U_inv', 'Lf_inv','U','R_inv','U_inv','L','U'])
                correct_positions_bool, current_positions = cubicle_positions()
            case 2:
                while [8,4] not in [current_positions[i] for i in range(len(correct_positions_bool)) if correct_positions_bool[i]]:
                    Sf = Sf*Uf*Df_inv
                    moves_performed.extend(['U, D_inv'])

                # Apply commutator
                Sf = Sf*Rf*Uf_inv*Lf_inv*Uf*Rf_inv*Uf_inv*Lf*Uf
                moves_performed.extend(['R, U_inv', 'Lf_inv','U','R_inv','U_inv','L','U'])
                correct_positions_bool, current_positions = cubicle_positions()
            case 4: 
                break


    # 8. Flip the entire Pocket Cube the solved white (Down) face to the Up face.
    # This is equivalent to performing:
    # RRLL
    
    # Reorient to get faces in their "most correct" spot
    correct_positions_bool, current_positions = cubicle_positions()
    while [8,4] != current_positions[0]:
        Sf = Sf*Uf*Df_inv
        moves_performed.extend(['U, D_inv'])
        correct_positions_bool, current_positions = cubicle_positions()

    # RRLL
    Sf = Sf*Rf*Rf*Lf*Lf
    moves_performed.extend(['R','R','L','L'])

    # 9. Since white is on our Up face, yellow will be our bottom face. Perform
    # D′ to get an incorrectly orientated cube into cubicle 7. Then perform the
    # commutator from (2) until it is correctly orientated:
    # [R, U ] = RU R′U ′

    # 10. Perform D′ to move the newly solved cube into cubicle 8.

    order = [22,24,23,21]
    for facelet in order:
        while (~Sf).array_form[22] != facelet:
            Sf = Sf*Rf*Uf*Rf_inv*Uf_inv
            moves_performed.extend(['R','U','R_inv','U_inv'])
        
        Sf = Sf*Df_inv
        moves_performed.append('D_inv')

    # 12. Perform U as needed to align the colors on the Front, Back, Left and Right Face
    while (~Sf).array_form != list(range(0,len(Sf.array_form))):
        Sf = Sf*Uf
        moves_performed.append('D_inv')

    print("Your Pocket Has Been Solved!")
    print("Moves to Solve:", moves_performed)
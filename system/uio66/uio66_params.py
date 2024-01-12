def get_uio66_params():
    # [atom_type] = m
    mass = {}
    mass['flexFF_Zn'] = 91.224
    mass['flexFF_C1'] = 12.011
    mass['flexFF_C2'] = 12.011
    mass['flexFF_C3'] = 12.011
    mass['flexFF_O1'] = 16.000
    mass['flexFF_O3'] = 16.000
    mass['flexFF_H1'] =  1.008
 
    # [atom_type] = q
    charge = {}
    charge['flexFF_Zn'] = 1.968
    charge['flexFF_C1'] = 0.630
    charge['flexFF_C2'] = -0.082
    charge['flexFF_C3'] = -0.065
    charge['flexFF_O1'] = -0.586
    charge['flexFF_O3'] = -0.992
    charge['flexFF_H1'] =  0.133

    # [atom_type-atom_type] = [funct, r0, k]
    bond_params = {}
    bond_params['intraFF_C1-intraFF_H1'] = [1, 0.1090, 154544.408]
    bond_params['intraFF_C1-intraFF_N']  = [1, 0.1340, 146958.816]
    bond_params['intraFF_C2-intraFF_N']  = [1, 0.1390, 114733.648]
    bond_params['intraFF_C2-intraFF_C2'] = [1, 0.1420, 120637.272]
    bond_params['intraFF_C2-intraFF_C5'] = [1, 0.1400, 146561.336]
    bond_params['intraFF_C5-intraFF_H5'] = [1, 0.1090, 151360.384]
    bond_params['intraFF_C5-intraFF_C6'] = [1, 0.1390, 153523.512]
    bond_params['intraFF_C6-intraFF_H6'] = [1, 0.1090, 150962.904]
    bond_params['intraFF_C6-intraFF_C6'] = [1, 0.1410, 142247.632]
    bond_params['intraFF_Zn-intraFF_N']  = [3, 0.1990, 109.0350, 19.8000]
    bond_params['repl_O-intraFF_Zn']     = [1, 0.1229, 476976.000]
    bond_params['repl_O-repl_H']         = [1, 0.0945, 462750.400]

    # [atom_type-atom_type-atom_type] = [funct, angle, k]
    angle_params = {}
    angle_params['intraFF_N-intraFF_C1-intraFF_H1']  = [1, 122.77, 227.610]
    angle_params['intraFF_N-intraFF_C1-intraFF_N']   = [1, 114.47, 473.880]
    angle_params['intraFF_N-intraFF_C2-intraFF_C5']  = [1, 131.01, 628.939]
    angle_params['intraFF_N-intraFF_C2-intraFF_C2']  = [1, 107.68, 510.406]
    angle_params['intraFF_C1-intraFF_N-intraFF_C2']  = [1, 105.09, 598.479]
    angle_params['intraFF_C2-intraFF_C5-intraFF_H5'] = [1, 121.52, 251.542]
    angle_params['intraFF_C2-intraFF_C5-intraFF_C6'] = [1, 117.01, 658.436]
    angle_params['intraFF_C5-intraFF_C6-intraFF_C6'] = [1, 121.67, 796.968]
    angle_params['intraFF_C5-intraFF_C6-intraFF_H6'] = [1, 119.17, 251.458]
    angle_params['intraFF_C6-intraFF_C6-intraFF_H6'] = [1, 119.15, 253.341]
    angle_params['intraFF_C6-intraFF_C5-intraFF_H5'] = [1, 121.48, 267.274]
    angle_params['intraFF_C2-intraFF_C2-intraFF_C5'] = [1, 120.93, 610.027]
    angle_params['intraFF_N-intraFF_Zn-intraFF_N']   = [1, 109.42, 76.1490]
    angle_params['intraFF_Zn-intraFF_N-intraFF_C1']  = [1, 126.76, 76.4840]
    angle_params['intraFF_Zn-intraFF_N-intraFF_C2']  = [1, 127.94, 78.8270]
    angle_params['intraFF_N-intraFF_Zn-repl_O']      = [1, 110.97, 76.3000]
    angle_params['intraFF_Zn-repl_O-repl_H']         = [1, 112.68, 76.3000]
    angle_params['repl_H-repl_O-repl_H']             = [1, 109.47, 383, 109.47, 383]

    # [atom_type-atom_type-atom_type-atom_type] = [funct, angle, k, n]        - periodic
    # [atom_type-atom_type-atom_type-atom_type] = [funct, c1, c2, c3, c4, c5] - fourier
    dihedral_params = {}
    dihedral_params['intraFF_N-intraFF_C2-intraFF_C5-intraFF_C6']  = [9, 180.00, 1.58992, 2]
    dihedral_params['intraFF_H1-intraFF_C1-intraFF_N-intraFF_C2']  = [9, 180.00, 9.91608, 2]
    dihedral_params['intraFF_C1-intraFF_N-intraFF_C2-intraFF_C2']  = [9, 180.00, 2.88696, 2]
    dihedral_params['intraFF_H5-intraFF_C5-intraFF_C2-intraFF_N']  = [9, 180.00, 0.92048, 2]
    dihedral_params['intraFF_C2-intraFF_C2-intraFF_C5-intraFF_H5'] = [9, 180.00, 1.08784, 2]
    dihedral_params['intraFF_C5-intraFF_C2-intraFF_C2-intraFF_C5'] = [9, 180.00, 2.59408, 2]
    dihedral_params['intraFF_H5-intraFF_C5-intraFF_C6-intraFF_C6'] = [9, 180.00, 0.92048, 2]
    dihedral_params['intraFF_H6-intraFF_C6-intraFF_C6-intraFF_C5'] = [9, 180.00, 2.34304, 2]
    dihedral_params['intraFF_C5-intraFF_C6-intraFF_C6-intraFF_C5'] = [9, 180.00, 4.43504, 2]
    dihedral_params['intraFF_N-intraFF_C2-intraFF_C2-intraFF_N']   = [9, 180.00, 4.60240, 2]
    dihedral_params['intraFF_N-intraFF_C2-intraFF_C2-intraFF_C5']  = [9, 180.00, 2.05016, 2]
    dihedral_params['intraFF_C1-intraFF_N-intraFF_C2-intraFF_C5']  = [9, 180.00, 2.46856, 2]
    dihedral_params['intraFF_C2-intraFF_C5-intraFF_C6-intraFF_H6'] = [9, 180.00, 5.18816, 2]
    dihedral_params['intraFF_C6-intraFF_C5-intraFF_C2-intraFF_C2'] = [9, 180.00, 0.92048, 2]
    dihedral_params['intraFF_C6-intraFF_C6-intraFF_C5-intraFF_C2'] = [9, 180.00, 2.42672, 2]
    dihedral_params['intraFF_N-intraFF_C1-intraFF_N-intraFF_C2']   = [9, 180.00, 9.62320, 2]
    dihedral_params['intraFF_C1-intraFF_N-intraFF_Zn-intraFF_N']   = [5, 12.63568, 9.45584, 0.33472, 0.00000]
    dihedral_params['intraFF_C2-intraFF_N-intraFF_Zn-intraFF_N']   = [5, 14.18376, -8.03328, 0.08368, 0.00000]

    return mass, charge, bond_params, angle_params, dihedral_params
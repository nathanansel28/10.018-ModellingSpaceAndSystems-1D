import scipy
from scipy.optimize import linprog
import pandas as pd

#ALL THE DATA (NEW)
df = pd.read_excel('Data.xlsx', sheet_name='Scenario1')
t = df.iloc[:,0]
D = df.iloc[:,1]
LCA1 = df.iloc[:,2]
LCA2 = df.iloc[:,3]
LCA3 = df.iloc[:,4]
c1 = df.iloc[:,5]
c2 = df.iloc[:,6]
c3 = df.iloc[:,7]

# EXECUTION
n = len(t)
Solution_Matrix = []

for i in range(n):
    # t1 = t[i]
    L1 = LCA1[i]
    L2 = LCA2[i]
    L3 = LCA2[i]
    Demand = D[i]
    C1 = -1 * c1[i]
    C2 = -1 * c2[i]
    C3 = -1 * c3[i] 

    # PART 1: CO2 FUNCTION
    coeff_CO2 = [L1, L2, L3]

    # PART 2: INEQUALITIES
    # ICE, EV, then H
    lhs_ineq = [
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]
    ]
    rhs_ineq = [
        C1,
        C2,
        C3
    ]

    # PART 3: EQUALITIES
    lhs_eq = [[1, 1, 1]]
    rhs_eq = [Demand]

    opt = linprog(c=coeff_CO2, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, method="highs")
    Solution_Matrix.append(list(opt.x))

# print(Solution_Matrix)

# for x in Solution_Matrix:
#     print(', '.join([str(n) for n in x]))

for x in Solution_Matrix:
    print('\t'.join([str(n) for n in x]))

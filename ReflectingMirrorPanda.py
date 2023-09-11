import numpy as np
import numpy.linalg as la
from numpy import transpose
from readonly.bearNecessities import *

verySmallNumber = 1e-14

def gsBasis4(A) :
    B = np.array(A, dtype=np.float_)
    B[:, 0] = B[:, 0] / la.norm(B[:, 0])
    B[:, 1] = B[:, 1] - B[:, 1] @ B[:, 0] * B[:, 0]
    if la.norm(B[:, 1]) > verySmallNumber :
        B[:, 1] = B[:, 1] / la.norm(B[:, 1])
    else :
        B[:, 1] = np.zeros_like(B[:, 1])
    return B

# In this function, you will return the transformation matrix T,
# having built it out of an orthonormal basis set E that you create from Bear's Basis
# and a transformation matrix in the mirror's coordinates TE.
def build_reflection_matrix(bearBasis) : # The parameter bearBasis is a 2×2 matrix that is passed to the function.
    # Use the gsBasis function on bearBasis to get the mirror's orthonormal basis.
    E = gsBasis4(bearBasis)
    # We now have E = the e-basis of the matrix BearBasis 

    # Write a matrix in component form that performs the mirror's reflection in the mirror's basis.
    # Recall, the mirror operates by negating the last component of a vector.
    # Replace a,b,c,d with appropriate values
    TE = np.array([[1, 0],
                   [0, -1]])
    Em = transpose(E)
    # Combine the matrices E and TE to produce your transformation matrix.
    TeEt = TE @ Em
    T = E @ TeEt 
    # Finally, we return the result. There is no need to change this line.
    return T


# ETeE-1 
# inv(A)
# transpose(A)
# gsBasis(A)
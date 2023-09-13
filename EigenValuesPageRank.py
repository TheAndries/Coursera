# PACKAGE
# Here are the imports again, just in case you need them.
# There is no need to edit or submit this cell.
import numpy as np
import numpy.linalg as la
from readonly.PageRankFunctions import *
np.set_printoptions(suppress=True)

# GRADED FUNCTION
# Complete this function to provide the PageRank for an arbitrarily sized internet.
# I.e. the principal eigenvector of the damped system, using the power iteration method.
# (Normalisation doesn't matter here)
# The functions inputs are the linkMatrix, and d the damping parameter - as defined in this worksheet.
# (The damping parameter, d, will be set by the function - no need to set this yourself.)
L = generate_internet(10)

def pageRank(linkMatrix, d) :
    L2 = np.array(linkMatrix)
    n = linkMatrix.shape[0]
    L2 = L.astype(int)

    d = 0.5 # Feel free to play with this parameter after running the code once.
    M = d * L + (1-d)/n * np.ones(n)

    r = 100 * np.ones(n) / n # Sets up this vector (6 entries of 1/6 × 100 each)
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r
        i += 1
    print(str(i) + " iterations to convergence.")
    r
    return r


def pageRank(linkMatrix, d) :
    L = np.array(linkMatrix)
    n = linkMatrix.shape[0]

    d = 0.5 # Feel free to play with this parameter after running the code once.
    M = d * L + (1-d)/n * np.ones(n)

    r = 100 * np.ones(n) / n # Sets up this vector (6 entries of 1/6 × 100 each)
    lastR = r
    r = M @ r
    i = 0
    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r
        i += 1
    print(str(i) + " iterations to convergence.")
    r
    return r
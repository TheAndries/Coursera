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
def pageRank(linkMatrix, d) :
    n = linkMatrix.shape[0]
    
    r = 100 * np.ones(10) / 10 # Sets up this vector (6 entries of 1/6 × 100 each)
    lastR = r
    r = n @ r
    i = 0
    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = n @ r
        i += 1
    print(str(i) + " iterations to convergence.")
    return r


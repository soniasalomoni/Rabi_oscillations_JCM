# --------------- #
# import packages #
# --------------- #

import numpy as np
from hypothesis import strategies as st
from hypothesis import given
from hypothesis import settings
import sys

sys.path.append('.')

# --------------- #
# import classes  #
# --------------- #

from Classes.Field import Field
from Classes.Atom import Atom
from Classes.System import System
from Classes.Simulation import Simulation

# --------------------- #
# start oracle testing  #
# --------------------- #

def W(simulation):
    """
    Compute the atomic inversion function using the analytical solution.

    Parameters:
    -----------
    simulation : Simulation
        the simulation instance we want to compute

    """
    W = - simulation.System.Field.PDF(0) # the cavity is empty

    # some useful shortcuts
    Omega2 = simulation.System.Omega**2
    Delta2 = simulation.System.Delta**2

    # we add all the contribution till the cut-off number of photons (N)
    for n in range(1,simulation.System.Field.cut_n):
        OmegaR = np.sqrt(Delta2 + n*Omega2)
        OmegaR2 = OmegaR**2
        t = simulation.time                            
        W = W - simulation.System.Field.PDF(n)*( Delta2/OmegaR2 + ((n*Omega2)/OmegaR2)*np.cos(t*OmegaR)) 

    return W

@settings(deadline=None) # Long tests are not converted into errors
@given(AVG_N = st.just(5), PDF_N = st.just("Poisson"), CUT_N = st.just(50), \
       Cg = st.just(1), Ce = st.just(0), OMEGA = st.just(1), DELTA = st.just(0), \
       TIME = st.just(100), TSTEP = st.just(0.01))
def test_simulation(AVG_N,PDF_N,CUT_N,Cg,Ce,OMEGA,DELTA,TIME,TSTEP):
    """
    Compare the analytical and numerical solution of the same system.
    """
    thr = 0.001

    field = Field(AVG_N,PDF_N,CUT_N)
    atom = Atom(Cg,Ce)
    system = System(field, atom, OMEGA, DELTA)
    simulation1 = Simulation(system,TIME,TSTEP)
    simulation2 = Simulation(system,TIME,TSTEP)
    simulation2.run()

    W1 = W(simulation1) # analytical solution
    W2 = simulation2.W_array # numerical solution
    assert(W1[0] - W2[0] < thr) , "Analytical and Numerical solutions don't coincide"




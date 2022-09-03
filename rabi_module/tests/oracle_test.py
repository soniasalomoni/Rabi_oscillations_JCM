# --------------- #
# oracle testing  #
# --------------- #

import numpy as np
from hypothesis import strategies as st
from hypothesis import given
from hypothesis import settings
import sys

sys.path.append('../.')
import rabi_module as rabi


def W_analytical(simulation):
    """
    Compute the atomic inversion function using the analytical solution.

    Parameters:
    -----------
    simulation : Simulation
        the simulation instance we want to compute

    """
    W = - simulation.system.field.PDF(0) # the cavity is empty

    # some useful shortcuts
    omega2 = simulation.system.omega**2
    delta2 = simulation.system.delta**2

    # we add all the contribution till the cut-off number of photons (N)
    for n in range(1,simulation.system.field.cut_n):
        omegaR = np.sqrt(delta2 + n*omega2)
        omegaR2 = omegaR**2
        t = simulation.time                            
        W = W - simulation.system.field.PDF(n)*( delta2/omegaR2 + ((n*omega2)/omegaR2)*np.cos(t*omegaR)) 

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

    field = rabi.Field(AVG_N,PDF_N,CUT_N)
    atom = rabi.Atom(Cg,Ce)
    system = rabi.System(field, atom, OMEGA, DELTA)
    simulation1 = rabi.Simulation(system,TIME,TSTEP)
    simulation2 = rabi.Simulation(system,TIME,TSTEP)
    simulation2.run()

    W1 = W_analytical(simulation1) # analytical solution
    W2 = simulation2.W_array # numerical solution
    assert(W1[0] - W2[0] < thr) , "Analytical and Numerical solutions don't coincide"

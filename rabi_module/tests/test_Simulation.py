
## --------------------- ##
## test Simulation class ##
## --------------------- ##

from re import T
from hypothesis import strategies as st
from hypothesis import given

import pytest
import sys

sys.path.append('../.')
import rabi_module as rabi

@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
    OMEGA = st.decimals(0,1), DELTA = st.decimals(-10,10),
    TIME = st.integers(50,100), TSTEP = st.decimals(0.001, 0.1))
def test_Simulation_init(PDF,OMEGA,DELTA, TIME, TSTEP):
    """
    This function tests if Simulation istances are correctly initialized
    when valid arguments are given to the Simulation constructor.

    GIVEN:  valid input parameters
    WHEN:   the Simulation constructor is called
    THEN:   a Simulation instance should be initialized without raising errors
    """
    field = rabi.Field(5,PDF,100)
    atom = rabi.Atom(1,0)
    system = rabi.System(field, atom, OMEGA, DELTA)
    rabi.Simulation(system, TIME, TSTEP)


@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
    OMEGA = st.decimals(0,1), DELTA = st.decimals(-10,10),)
def test_Simulation_raises(PDF,OMEGA,DELTA):
    """
    This function tests if errors are correctly raised when 
    invalid parameters are given to System constructor.

    GIVEN:  invalid input parameters
    WHEN:   the Simulation constructor is called
    THEN:   ValueErrors should be raised
    """
    field = rabi.Field(5,PDF,100)
    atom = rabi.Atom(1,0)
    system = rabi.System(field, atom, OMEGA, DELTA)

    with pytest.raises(ValueError):
        rabi.Simulation(system, -1, 0.01)
    with pytest.raises(ValueError):
        rabi.Simulation(system, 100, -0.01)
    with pytest.raises(ValueError):
        rabi.Simulation(system, 10, 1)
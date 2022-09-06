
## ----------------- ##
## test System class ##
## ----------------- ##

import numpy as np
from hypothesis import strategies as st
from hypothesis import given

import pytest
import sys

sys.path.append('../.')
import rabi_module as rabi


@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
    OMEGA = st.decimals(0,1), DELTA = st.decimals(-10,10))
def test_System_init(PDF, OMEGA, DELTA):
    """
    This function tests if System istances are correctly initialized
    when valid arguments are given to the System constructor.

    GIVEN:  valid input parameters
    WHEN:   the System constructor is called
    THEN:   a System instance should be initialized without raising errors
    """
    field = rabi.Field(5,PDF,100)
    atom = rabi.Atom(1,0)
    rabi.System(field, atom, OMEGA, DELTA)


@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
    OMEGA = st.floats(0,1), DELTA = st.floats(-10,10),
    RANDN = st.integers(0,10), RANDN2 = st.integers(0,10))
def test_System_prop(PDF, OMEGA, DELTA, RANDN, RANDN2):
    """
    This function tests if the model implemented in System is physical.

    GIVEN:  different valid System instances
    WHEN:   the method rabi.model is called
    THEN:   the time evolution of the atomic states has physical meaning
    """
    field = rabi.Field(5,PDF,100)
    atom = rabi.Atom(1,0)
    system = rabi.System(field, atom, OMEGA, DELTA)

    z = [atom.Cg, atom.Ce]
    t = np.arange(0,50,0.1)
    # we use different number of photons RANDN and RANDN2
    dgdt, dedt = system.rabi_model(z, t, RANDN)
    dgdt2, dedt2 = system.rabi_model(z, t, RANDN2)

    if system.omega == 0 and system.delta == 0:
        # if the atom and the field do not interact (omega = 0) and there is no detuning (delta = 0)
        # the atomic state remains constant (dgdt = dedt = 0)
        assert(dgdt == 0 and dedt == 0)
    if system.omega == 0:
        # if the atom and the field do not interact (omega = 0), the time evolution of the atomic
        # state doesn't depend on the number of photons
        assert(dgdt == dgdt2 and dedt == dedt2) 
    if system.delta == 0:
        # if there is no detuning, the time evolution of the atomic state depends just on the
        # number of photons in the cavity (since omega is the same) and the variations are 
        # proportional to it
        if RANDN > RANDN2:
            assert(dgdt > dgdt2 and dedt > dedt2)
        if RANDN < RANDN2:
            assert(dgdt < dgdt2 and dedt < dedt2)
        if RANDN == RANDN2:
            assert(dgdt == dgdt2 and dedt == dedt2)


@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
       DELTA = st.decimals(0,10))
def test_System_raises(PDF,DELTA):
    """
    This function tests if errors are correctly raised when 
    invalid parameters are given to System constructor.

    GIVEN:  invalid input parameters
    WHEN:   the System constructor is called
    THEN:   ValueErrors should be raised
    """
    field = rabi.Field(5,PDF,100)
    atom = rabi.Atom(1,0)
    with pytest.raises(ValueError):
        rabi.System(field, atom, -1, DELTA)

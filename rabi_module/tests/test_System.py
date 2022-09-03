
## ----------------- ##
## test System class ##
## ----------------- ##

from hypothesis import strategies as st
from hypothesis import given

import pytest
import sys

sys.path.append('../.')
import rabi_module as rabi

@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
    OMEGA = st.decimals(0,1), DELTA = st.decimals(-10,10))
def test_System_init(PDF,OMEGA,DELTA):
    """
    This function tests if System istances are correctly initialized
    when valid arguments are given to the System constructor.
    """
    field = rabi.Field(5,PDF,100)
    atom = rabi.Atom(1,0)
    rabi.System(field, atom, OMEGA, DELTA)

@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
       DELTA = st.decimals(0,10))
def test_System_raises(PDF,DELTA):
    """
    This function tests if errors are correctly raised when 
    invalid parameters are given to System constructor.
    """
    field = rabi.Field(5,PDF,100)
    atom = rabi.Atom(1,0)
    with pytest.raises(ValueError):
        rabi.System(field, atom, -1, DELTA)

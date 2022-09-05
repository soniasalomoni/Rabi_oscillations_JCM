## --------------- ##
## test Atom class ##
## --------------- ##

from hypothesis import strategies as st
from hypothesis import given

import numpy as np
import pytest
import sys

sys.path.append('../.')
import rabi_module as rabi

# ----------------------------------------------------- #

@given(coeff = st.decimals(0,1))
def test_Atom_init(coeff):
    """
    This function tests if Atom istances are correctly initialized
    when valid states are given to Atom constructor.
    """
    C1 = coeff
    C2 = np.sqrt(1-coeff**2)
    default_atom = rabi.Atom()
    assert(default_atom.Cg == 1 and default_atom.Ce == 0), "By default the atom should be in the ground state"
    first_atom = rabi.Atom(C1,C2)
    second_atom = rabi.Atom(C2,C1)  
    assert(first_atom.Cg == second_atom.Ce and first_atom.Ce == second_atom.Cg), "Initial states are not correctly initialized"  

def test_Atom_raises():
    """
    This function tests if errors are correctly raised when 
    invalid states are given to Atom constructor.
    """
    with pytest.raises(ValueError):
        rabi.Atom(0,0)
    with pytest.raises(ValueError):
        rabi.Atom(1,1)
    with pytest.raises(ValueError):
        rabi.Atom(0,-1)
    with pytest.raises(ValueError):
        rabi.Atom(0,10)
    
    
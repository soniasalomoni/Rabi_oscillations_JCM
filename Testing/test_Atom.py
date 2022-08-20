## --------------- ##
## test Atom class ##
## --------------- ##

from hypothesis import strategies as st
from hypothesis import given

import numpy as np
import pytest
import sys

sys.path.append('.')
from Classes.Atom import *

# ----------------------------------------------------- #

@given(coeff = st.decimals(0,1))
def test_Atom_init(coeff):
    """
    This function tests if Atom istances are correctly initialized
    when valid states are given to Atom constructor.
    """
    C1 = coeff
    C2 = np.sqrt(1-coeff**2)
    Atom(C1,C2)
    Atom(C2,C1)    

def test_Atom_raises():
    """
    This function tests if errors are correctly raised when 
    invalid states are given to Atom constructor.
    """
    with pytest.raises(ValueError):
        Atom(0,0)
    with pytest.raises(ValueError):
        Atom(1,1)
    with pytest.raises(ValueError):
        Atom(0,-1)
    with pytest.raises(ValueError):
        Atom(0,10)
    
    
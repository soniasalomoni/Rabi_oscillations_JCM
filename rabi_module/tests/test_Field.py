## ---------------- ##
## test Field class ##
## ---------------- ##

from hypothesis import strategies as st
from hypothesis import given

import numpy as np
import pytest
import sys

sys.path.append('../.')
import rabi_module as rabi

def is_PDF(pdf, N):
    """
    This function checks if the function pdf is a Probability Density Function:
    - pdf(n) is non-negative for all possible values of n.
    - The sum of pdf(n) over all possible values of n is normalized.
    Because we're dealing with PDF of photons, n is a positive integer
    within the range [0,N].

    Parameters:
    -----------
    pdf : callable(n)
        the function to be tested
    N : int
        the maximum value for n

    """
    norm = 0
    for n in range(0,N):
        if pdf(n) < 0:
            return False
        norm = norm + pdf(n)
    if abs(norm-1) > 0.01:
        return False
    else:
        return True

@given(AVG_N = st.integers(0,50), PDF_N = st.just("Dirac"), CUT_N = st.integers(100,300))
def test_Dirac_PDF(AVG_N,PDF_N,CUT_N):
    """
    This function tests if rabi.field.Dirac is a PDF
    """
    field = rabi.Field(AVG_N,PDF_N,CUT_N)
    bool = is_PDF(field.Dirac,field.cut_n)
    assert(bool == True) , "Field.Dirac is not a PDF"

@given(AVG_N = st.integers(0,50), PDF_N = st.just("Poisson"), CUT_N = st.integers(100,300))
def test_Poisson_PDF(AVG_N,PDF_N,CUT_N):
    """
    This function tests if rabi.field.Poisson is a PDF
    """
    field = rabi.Field(AVG_N,PDF_N,CUT_N)
    bool = is_PDF(field.Poisson,field.cut_n)
    assert(bool == True) , "Field.Poisson is not a PDF"

@given(AVG_N = st.integers(0,20), PDF_N = st.just("BoseEinstein"), CUT_N = st.integers(100,300))
def test_BoseEinstein_PDF(AVG_N,PDF_N,CUT_N):
    """
    This function tests if rabi.field.BoseEinstein is a PDF
    """
    field = rabi.Field(AVG_N,PDF_N,CUT_N)
    bool = is_PDF(field.BoseEinstein,field.cut_n)
    assert(bool == True) , "Field.BoseEinstein is not a PDF"

@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]))
def test_Field_raises(PDF):
    """
    This function tests if errors are correctly raised when 
    invalid parameters are given to Field constructor.
    """
    with pytest.raises(ValueError):
        rabi.Field(-1,PDF,100)
    with pytest.raises(ValueError):
        rabi.Field(1,PDF,-1)
    with pytest.raises(ValueError):
        rabi.Field(-100,PDF,-1)
    with pytest.raises(ValueError):
        rabi.Field(100,PDF,1)

def test_Field_thr():
    """
    This function tests if errors are correctly raised when 
    the cutoff number of photons is not large enough compared
    to the average number of photons.
    """      
    rabi.Field(99,"Dirac",100)
    with pytest.raises(ValueError):
        rabi.Field(99,"Poisson",100)
    with pytest.raises(ValueError):
        rabi.Field(99,"BoseEinstein",100)







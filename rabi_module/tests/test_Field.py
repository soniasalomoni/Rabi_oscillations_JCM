## ---------------- ##
## test Field class ##
## ---------------- ##


from re import A
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

@given(AVG_N = st.integers(0,50), PDF_N = st.just("Dirac"), CUT_N = st.integers(100,300),
    RANDN = st.integers(0,100))
def test_Dirac_prop(AVG_N,PDF_N,CUT_N, RANDN):
    """
    This function tests if rabi.field.Dirac models a Dirac PDF,
    thus it should return 1 if n equals the average number of photons
    and 0 in any other case.
    """
    field = rabi.Field(AVG_N,PDF_N,CUT_N)
    assert(field.Dirac(AVG_N) == 1)
    if RANDN != AVG_N:
        assert(field.Dirac(RANDN) == 0)

@given(AVG_N = st.integers(0,50), PDF_N = st.just("Poisson"), CUT_N = st.integers(100,300),
    RANDN = st.integers(0,100))
def test_Poisson_prop(AVG_N,PDF_N,CUT_N, RANDN):
    """
    This function tests if rabi.field.Dirac models a Poisson PDF,
    thus its main mathematical properties are checked
    """
    field = rabi.Field(AVG_N,PDF_N,CUT_N)
    if AVG_N != 0:
        # if the average number of photons is not 0, any probability is greater than 0
        assert(field.Poisson(RANDN) > 0)
    else:
        # if the average number of photons is 0, the Poisson PDF is like a Dirac one
        assert(field.Poisson(RANDN) == field.Dirac(RANDN))

    # for the Poisson PDF the average value is also equal to the variance
    values = np.array(500)
    probs = field.Poisson(values)
    assert(np.var(probs) - AVG_N < 0.001)

@given(AVG_N = st.integers(0,20), PDF_N = st.just("BoseEinstein"), CUT_N = st.integers(100,300),
    RANDN = st.integers(0,100))
def test_BoseEinstein_prop(AVG_N,PDF_N,CUT_N, RANDN):
    """
    This function tests if rabi.field.Dirac models a Poisson PDF,
    thus its main mathematical properties are checked
    """
    field = rabi.Field(AVG_N,PDF_N,CUT_N)
    if AVG_N !=0:
        # if the average number of photons is not 0, any probability is greater than 0
        assert(field.BoseEinstein(RANDN) > 0)
        # and the PDF is strictly descending
        assert(field.BoseEinstein(RANDN) > field.BoseEinstein(RANDN+1))
        # check the probability for 0 photons
        assert(field.BoseEinstein(0) - 1/(1+AVG_N) < 0.001)
    else:
        # if the average number of photons is 0, the PDF is like a Dirac one
        assert(field.BoseEinstein(RANDN) == field.Dirac(RANDN))

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







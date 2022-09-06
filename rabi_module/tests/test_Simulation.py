
## --------------------- ##
## test Simulation class ##
## --------------------- ##


from hypothesis import strategies as st
from hypothesis import given
from hypothesis import settings

import pytest
import sys


sys.path.append('../.')
import rabi_module as rabi

@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
    OMEGA = st.decimals(0,1), DELTA = st.decimals(0,10),
    TIME = st.just(100), TSTEP = st.just(0.01))
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

@settings(deadline=None) # Long tests are not converted into errors
@given(PDF = st.sampled_from(["Dirac","Poisson","BoseEinstein"]),
    OMEGA = st.just(1), DELTA = st.just(0),
    TIME = st.just(50), TSTEP = st.just(0.01))
def test_Simulation_prop(PDF, OMEGA, DELTA, TIME, TSTEP):
    """
    This function tests if during a Simulation some parameters evolve correctly
    or remain contant as expected

    GIVEN:  two identical Simulation objects
    WHEN:   one object runs the simulation
    THEN:   the internal parameters evolve correctly
            or remain constant as expected
    """
    field = rabi.Field(5,PDF,70)
    atom = rabi.Atom(1,0)
    system = rabi.System(field, atom, OMEGA, DELTA)
    simulation_0 = rabi.Simulation(system, TIME, TSTEP)
    simulation_t = rabi.Simulation(system, TIME, TSTEP)

    simulation_t.run()

    # field is constant
    assert(simulation_0.system.field.avg_n == simulation_t.system.field.avg_n)
    assert(simulation_0.system.field.pdf_n == simulation_t.system.field.pdf_n)
    assert(simulation_0.system.field.cut_n == simulation_t.system.field.cut_n)

    # atom evolves to valid states
    assert(simulation_t.system.atom.Cg >= 0 and simulation_t.system.atom.Cg <= 1)
    assert(simulation_t.system.atom.Ce >= 0 and simulation_t.system.atom.Ce <= 1)
    assert(simulation_t.system.atom.Ce**2 + simulation_t.system.atom.Cg**2 - 1 < 0.001)

    # system is constant
    assert(simulation_0.system.omega == simulation_t.system.omega)
    assert(simulation_0.system.delta == simulation_t.system.delta)

    # simulation is constant
    assert(all(simulation_0.time == simulation_t.time))

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
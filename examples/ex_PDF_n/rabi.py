
import matplotlib.pyplot as plt
import sys

sys.path.append('../../.')
import rabi_module as rabi

print('\t ... ', end='\r')

# reading
field_info, atom_info, system_info, simulation_info, saving_info = rabi.read_txt()

# unpacking
AVG_N, PDF_N, CUT_N = field_info
Cg_0, Ce_0 = atom_info
OMEGA, DELTA = system_info
TMAX, TSTEP = simulation_info
SAVE_TXT, SAVE_PNG, OUT_LABEL = saving_info

# creating objects
field = rabi.Field(AVG_N,PDF_N,CUT_N)
atom = rabi.Atom(Cg_0,Ce_0)
system = rabi.System(field, atom, OMEGA, DELTA)
simulation = rabi.Simulation(system,TMAX,TSTEP)

# running
simulation.run()

# plotting
fig = rabi.plot_W(simulation)

# saving
if SAVE_TXT == True:
    rabi.save_txt(simulation, OUT_LABEL)

if SAVE_PNG == True:
    plt.savefig('./{}.png'.format(OUT_LABEL))

print('Rabi simulation completed.')


import matplotlib.pyplot as plt
import sys

sys.path.append('../../.')
import rabi_module as rabi

print('\t ... ', end='\r')

# reading
simulation, saving_info = rabi.read_txt()
SAVE_TXT, SAVE_PNG, OUT_LABEL = saving_info

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


import numpy as np

# define saving function

def save_txt(simulation, input_file = "input.txt", label = "output"):
    """
    Save simulation results (atomic inversion function) to a .txt file.
    At the beginning of the file, input parameters are printed as comments.

    Parameters:
    -----------
    simulation : Simulation 
        the Simulation instance whose inversion function is saved
    input_file : str 
        the name of the input file from which the parameters were read
    label : str
        the name of the .txt output file

    """

    fin = open(input_file,'r+')
    fout = open('./{}.txt'.format(label),'w+')
    # write simulation input parameters
    fout.write('# This output.txt file was obtained running a\n# simulation with these input parameters\n\n')
    for line in fin.readlines():
        fout.write('# ' + line)
    # write formatted simulation output
    fout.write('\n\n# -------------------------------------------- #\n\n')
    fout.write('# [Time]     [Atomic inversion function] \n\n')
    for t in range(0,len(simulation.time)):
        fout.write('   ' + "{:.2f}".format(np.round(simulation.time[t],2)).rjust(5,'0') + \
                    "\t" + "{:+.10f}".format(simulation.W_array[t]) + '\n')

import configparser

# define reading function

def read_txt(input_file = "input.txt"):
    """
    Reads input parameters from a .txt file

    Parameters:
    -----------
    input_file : str 
        the name of the input file from which the parameters are read
    
    Returns:
    --------
    read_info : tuple
        a tuple containing all the readed information, oganized as:

        read_info = (field_info, atom_info, system_info, simulation_info, saving_info)

        field_info = (AVG_N, PDF_N, CUT_N)
        atom_info = (Cg_0, Ce_0)
        system_info = (OMEGA, DELTA)
        simulation_info = (TMAX, TSTEP)
        saving_info = (SAVE_TXT, SAVE_PNG, OUT_LABEL)
        
    """
    
    # initialize config 
    config = configparser.ConfigParser()
    config.read(input_file)

    # --------------------- #
    # initialize parameters #
    # --------------------- #

    AVG_N = int(config.get('field','avg_n'))
    PDF_N = config.get('field','pdf_n')
    CUT_N = int(config.get('field','cut_n'))

    field_info = (AVG_N, PDF_N, CUT_N)

    Cg_0 = float(config.get('atom','Cg'))
    Ce_0 = float(config.get('atom','Ce'))

    atom_info = (Cg_0, Ce_0)

    OMEGA = float(config.get('interaction','int_coupling'))
    DELTA = float(config.get('interaction','int_detuning'))

    system_info = (OMEGA, DELTA)

    TMAX = int(config.get('simulation','time'))
    TSTEP = float(config.get('simulation','step'))

    simulation_info = (TMAX, TSTEP)

    SAVE_TXT = bool(config.get('output','save_txt'))
    SAVE_PNG = bool(config.get('output','save_png'))
    OUT_LABEL = config.get('output','out_label')

    saving_info = (SAVE_TXT, SAVE_PNG, OUT_LABEL)

    read_info = (field_info, atom_info, system_info, simulation_info, saving_info)

    return read_info
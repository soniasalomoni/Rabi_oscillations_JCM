# -*- coding: utf-8 -*-
"""
Created on Mon July 09 15:50:52 2021
@author: Sonia Salomoni
"""
# --------------- #
# import packages #
# --------------- #

import configparser
import matplotlib.pyplot as plt
from sys import argv

# --------------- #
# import classes  #
# --------------- #

from Classes.Field import Field
from Classes.Atom import Atom
from Classes.System import System
from Classes.Simulation import Simulation

# ----------------- #
# import utilities  #
# ----------------- #

from Utilities.saving import save_txt
from Utilities.plotting import plot_W

print('\t ... ', end='\r')

# ----------------- #
# initialize config #
# ----------------- #

config = configparser.ConfigParser()

# is given the possibility to specify the configuration file as second argument in the bash command: sys.argv[1]  
# The default configuration file if not specified through sys.argv[1] is "input.txt".

if len(argv)>=2:
    config.read(argv[1])
else:
    config.read("Utilities/input.txt")

# --------------------- #
# initialize parameters #
# --------------------- #

AVG_N = int(config.get('field','avg_n'))
PDF_N = config.get('field','pdf_n')
CUT_N = int(config.get('field','cut_n'))

Cg_0 = float(config.get('atom','Cg'))
Ce_0 = float(config.get('atom','Ce'))

OMEGA = float(config.get('interaction','int_coupling'))
DELTA = float(config.get('interaction','int_detuning'))

TMAX = int(config.get('simulation','time'))
TSTEP = float(config.get('simulation','step'))

SAVE_TXT = bool(config.get('output','save_txt'))
SAVE_PNG = bool(config.get('output','save_png'))
OUT_LABEL = config.get('output','out_label')

# -------------------------- #
# initialize class instances #
# -------------------------- #

field = Field(AVG_N,PDF_N,CUT_N)
atom = Atom(Cg_0,Ce_0)
system = System(field, atom, OMEGA, DELTA)
simulation = Simulation(system,TMAX,TSTEP)

# ------------------ #
# run the simulation #
# ------------------ #

simulation.run()

# ---------------- #
# plot the results #
# ---------------- #

fig = plot_W(simulation)

# ---------------- #
# save the results #
# ---------------- #
if SAVE_TXT == True:
    save_txt(simulation, OUT_LABEL)

if SAVE_PNG == True:
    plt.savefig('Output/{}.png'.format(OUT_LABEL))

print('Rabi simulation completed.')
print('Check the Output directory for results.')


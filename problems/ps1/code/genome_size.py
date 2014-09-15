# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np
import pandas as pd

bp_length = 3.4e-10
bp_mass = 1e-24

print("Viruses")
fn = "viruses.txt"
data = pd.read_csv(fn, sep="\t")
sizes = np.array(data["Size (Kb)"].where(data["Size (Kb)"] != "-"),
                 dtype=float)
sizes = sizes[np.isfinite(sizes)]
genome_size = np.mean(sizes) * 1000
print("The genome size is {0} bp".format(genome_size))
print("This stretches {0} m/cell".format(genome_size * bp_length))
print("This weighs {0} kg/cell".format(genome_size * bp_mass))
n_cell = 1e30
n_bp = n_cell * genome_size
print("Given {0:e} cells, there are a total of {1:e} base pairs"
      .format(n_cell, n_bp))
tot_length = n_bp * bp_length
tot_mass = n_bp * bp_mass
print("This will stretch {0:e}m = {1:e}ly".format(tot_length,
                                                  tot_length*1.057e-16))
print("and weigh {0:e}kg".format(tot_mass))
print()

print("Prokaryotes")
fn = "prokaryotes.txt"
data = pd.read_csv(fn, sep="\t")
sizes = np.array(data["Size (Mb)"], dtype=float)
sizes = sizes[np.isfinite(sizes)]
genome_size = np.mean(sizes) * 1e6
print("The genome size is {0} bp".format(genome_size))
print("This stretches {0} m/cell".format(genome_size * bp_length))
print("This weighs {0} kg/cell".format(genome_size * bp_mass))
n_cell = 1e30
n_bp = n_cell * genome_size
print("Given {0:e} cells, there are a total of {1:e} base pairs"
      .format(n_cell, n_bp))
tot_length = n_bp * bp_length
tot_mass = n_bp * bp_mass
print("This will stretch {0:e}m = {1:e}ly".format(tot_length,
                                                  tot_length*1.057e-16))
print("and weigh {0:e}kg".format(tot_mass))
print()

print("Humans")
genome_size = 3e9
print("The genome size is {0} bp".format(genome_size))
print("This stretches {0} m/cell".format(genome_size * bp_length))
print("This weighs {0} kg/cell".format(genome_size * bp_mass))
n_cell = 1e13
n_bp = n_cell * genome_size
print("Given {0:e} cells, there are a total of {1:e} base pairs per human"
      .format(n_cell, n_bp))
tot_length = n_bp * bp_length
tot_mass = n_bp * bp_mass
print("This will stretch {0:e}m = {1:e}ly".format(tot_length,
                                                  tot_length*1.057e-16))
print("and weigh {0:e}kg".format(tot_mass))
print()
tot_length *= 6e9
tot_mass *= 6e9
print("All humans: {0:e}m = {1:e}ly".format(tot_length, tot_length*1.057e-16))
print("and weigh {0:e}kg".format(tot_mass))

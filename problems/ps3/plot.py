#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl

from astropy import units as u
from astropy import constants as const

D = 5 * u.micrometer ** 2 / u.s


def run(R, n, cinf, **fmt):
    k = (n / (60. * u.s) * u.min / u.micrometer / const.N_A) \
        .to(u.micromole * u.min / (u.s * u.micrometer))
    w = 4 * np.pi * D * R * cinf
    v = (w / k).to(u.micrometer / u.min)
    print("k = ", k)
    print("w = ", w.to(u.micromole / u.s))
    print("v = ", v)
    print()

    s = np.linspace(float(R / u.nm), 250, 5000) * u.nm
    c = (cinf - w / (4 * np.pi * D * s) * np.exp(-0.5 * v * s / D)) \
        / (1e-3 * u.mole / u.m**3)
    pl.plot(np.log10(s.value), c.value, "k", **fmt)

# Microtubules.
print("Microtubules")
cinf = 10e-3 * u.mole / u.m**3
R = 12.5 * u.nm
n = 1690.
run(R, n, cinf, lw=2)

# Actin.
print("Actin")
cinf = 20e-3 * u.mole / u.m**3
R = 4 * u.nm
n = 370.
run(R, n, cinf, lw=2, ls="--")

pl.xlabel(r"$\log_{10} s / \mathrm{nm}$")
pl.ylabel(r"$c(s) / \mathrm{\mu M}$")
fig = pl.gcf()
fig.subplots_adjust(bottom=0.15, top=0.97, right=0.98)
pl.savefig("c.pdf")

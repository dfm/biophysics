#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as pl


def h(x, y):
    return x*x + x*y - 2*y*y


fig = pl.figure(figsize=(10, 5))

x = np.linspace(0, 1, 5000)
y = np.linspace(0, 1, 5)
ax = fig.add_subplot(121)
[ax.plot(x, h(x, y0), label="$y={0:.2f}$".format(y0), lw=2) for y0 in y]
ax.legend(fontsize=10, loc=2)
ax.set_xlabel("$x$")
ax.set_ylabel(r"$h(x,\,y)$")

y = np.linspace(0, 1, 5000)
x = np.linspace(0, 1, 5)
ax = fig.add_subplot(122)
[ax.plot(y, h(x0, y), label="$x={0:.2f}$".format(x0), lw=2) for x0 in x]
ax.legend(fontsize=10, loc=3)
ax.set_yticklabels([])
ax.set_xlabel("$y$")

fig.subplots_adjust(bottom=0.15, top=0.97)
fig.savefig("figure.pdf")

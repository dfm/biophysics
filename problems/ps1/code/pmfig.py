#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import matplotlib.pyplot as pl

pl.figure(figsize=(10, 4))

bg = dict(color="b", alpha=0.5, lw=0, edgecolor="none")
scat = dict(color="r", alpha=0.5, lw=0, edgecolor="none")

pl.fill_between([4.333, 5, 8], [0.05, 0.6, 0], [-0.05, -0.6, 0], **scat)

pl.fill_between([1, 2], [1, 1], [-1, -1], **bg)

pl.fill_between([2, 3, 5], [1, 1, -0.4], [0.9, 0.9, -0.5], **bg)
pl.fill_between([2, 3, 5], [-0.9, -0.9, 0.5], [-1, -1, 0.4], **bg)

pl.fill_between([5, 8], [-0.4, 0], [-0.5, 0], **bg)
pl.fill_between([5, 8], [0.4, 0], [0.5, 0], **bg)

pl.plot([2, 2], [-0.9, 0.9], "k", lw=2)
pl.plot([2, 2], [1, 1.5], "k", lw=2)
pl.plot([2, 2], [-1, -1.5], "k", lw=2)

pl.plot([3, 3], [-1.5, 1.5], "k", lw=2)

pl.plot([4.333, 4.333], [-0.1, 0.1], "k", lw=2)
pl.plot([4.333, 4.333], [-1.5, 1.5], ":k")

pl.plot([5, 5], [-1.5, 1.5], "k", lw=2)

pl.plot([6, 6], [-1.5, 1.5], ":k")
pl.plot([6, 6], [-0.32, -0.28], "k", lw=2)
pl.plot([6, 6], [0.32, 0.28], "k", lw=2)

ax = pl.gca()
ax.annotate("(a)", xy=(2, 1.5), xytext=(0, 10), textcoords="offset points",
            ha="center")
ax.annotate("(b)", xy=(3, 1.5), xytext=(0, 10), textcoords="offset points",
            ha="center")
ax.annotate("(c)", xy=(4.33, 1.5), xytext=(0, 10), textcoords="offset points",
            ha="center")
ax.annotate("(d)", xy=(5, 1.5), xytext=(0, 10), textcoords="offset points",
            ha="center")
ax.annotate("(e)", xy=(6, 1.5), xytext=(0, 10), textcoords="offset points",
            ha="center")

pl.ylim(-1.5, 2)
pl.axis("off")
pl.gcf().subplots_adjust(left=0, right=1, bottom=0, top=1)

pl.savefig("../phase_micro.pdf")

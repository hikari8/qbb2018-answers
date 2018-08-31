#!/usr/bin/env python3

"""
Usage: ./generalized.py <gene_name> <samples.csv> <ctab_dir>
Create a timecourse
ex: ./for_males.py FBtr0331261 ~/qbb2018/samples.csv ~/data/results/stringtie/
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
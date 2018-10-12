#!/usr/bin/env python3

"""
./automate.py
"""

import os

list_of_files = [
    "plink.Caffeine.qassoc",
    "plink.Calcium_Chloride.qassoc",
    "plink.Cisplatin.qassoc",
    "plink.Cobalt_Chloride.qassoc",
    "plink.Congo_red.qassoc",
    "plink.Copper.qassoc",
    "plink.Cycloheximide.qassoc",
    "plink.Diamide.qassoc",
    "plink.E6_Berbamine.qassoc",
    "plink.Ethanol.qassoc",
    "plink.Formamide.qassoc",
    "plink.Galactose.qassoc",
    "plink.Hydrogen_Peroxide.qassoc",
    "plink.Hydroquinone.qassoc",
    "plink.Hydroxyurea.qassoc",
    "plink.Indoleacetic_Acid.qassoc",
    "plink.Lactate.qassoc",
    "plink.Lactose.qassoc",
    "plink.Lithium_Chloride.qassoc",
    "plink.Magnesium_Chloride.qassoc",
    "plink.Magnesium_Sulfate.qassoc",
    "plink.Maltose.qassoc",
    "plink.Mannose.qassoc",
    "plink.Menadione.qassoc",
    "plink.Neomycin.qassoc",
    "plink.Paraquat.qassoc",
    "plink.Raffinose.qassoc",
    "plink.SDS.qassoc",
    "plink.Sorbitol.qassoc",
    "plink.Trehalose.qassoc",
    "plink.Tunicamycin.qassoc",
    "plink.Xylose.qassoc",
    "plink.YNB_ph3.qassoc",
    "plink.YNB_ph8.qassoc",
    "plink.YPD.qassoc",
    "plink.YPD_15C.qassoc",
    "plink.YPD_37C.qassoc",
    "plink.YPD_4C.qassoc",
    "plink.Zeocin.qassoc",
    "plink.x4_NQO.qassoc",
    "plink.x4_Hydroxybenzaldehyde.qassoc",
    "plink.x5_Fluorocytosine.qassoc",
    "plink.x5_Fluorouracil.qassoc",
    "plink.x6_Azauracil.qassoc",
    "plink.YNB.qassoc",
    ]

for i in range(len(list_of_files)):
    os.system("./manhattan_pandasway.py " + str(list_of_files[i]))
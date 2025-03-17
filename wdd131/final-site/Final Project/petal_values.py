"""Assigning numerical values to petal descriptors in order to determine which flower it is"""

#importing spreadsheet
import pandas as pd

# URL of the Google Sheets CSV export
url = "https://docs.google.com/spreadsheets/d/1M4GVrWIwBFvq14DaJubvQ5bRJ-9mTB1Mp2Hh9spKd08/export?format=csv"

# Reading the spreadsheet
df = pd.read_csv(url)

# Flower types
flowers = ["daisy", "orchid", "violet"]

# Petal descriptors

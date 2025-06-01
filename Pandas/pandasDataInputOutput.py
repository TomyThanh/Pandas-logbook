import numpy as np
import pandas as pd

tables = pd.read_html("https://www.fdic.gov/bank-failures/failed-bank-list")
print(tables[0].head())




















import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("animal_data_dirty1.csv", sep=';', skiprows=2)

first_rows = df.head()
print(first_rows)

print(df.columns)
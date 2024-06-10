# importing all the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path_to_file = "/Users/abhijaydas/Desktop/python/machinelearning_project1 /magic04.data"
cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
magic04_data = pd.read_csv(path_to_file , names = cols)
magic04_data.head()
print(magic04_data)






# %% Pandas interative test
import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)

# %% Import data

data = pd.read_csv('titanic3.csv')
data.info
# %%

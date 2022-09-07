# %% Interactive Jupyter-like Python test

a = 13
print('a = ',a)
print('a^2 = ',a**2)


# %% Second cell

print('This is 2nd cell')

# %%
# Make a big array

import numpy as np

n = np.arange(25).reshape(5,5)
print(n)
# %%
n2 = n ** 2
print(n2)
# %%

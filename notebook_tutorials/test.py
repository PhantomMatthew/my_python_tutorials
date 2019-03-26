import numpy as np
import pandas as pd

persontype = np.dtype([('name', 'S32'), ('age', 'i'), ('weight', 'f')], align=True )

a = np.array([("Zhang",32,75.5), ("Wang",24,65.2)], dtype=persontype)
print(a)

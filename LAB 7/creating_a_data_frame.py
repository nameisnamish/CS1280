import pandas as pd
import numpy as np
# Create a DataFrame from a dictionary
data = {'Name': ['Ram', 'Robert','Rahim'],
	'Age': [25, 30, 35],
	'City': ['Ayodya', 'Chennai', 'Delhi']}
df = pd.DataFrame(data)
print(df)

import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'seeds_data.csv') 
data = pd.read_csv(my_file)
scale= StandardScaler()
 
# standardization of dependent variables
scaled_data = scale.fit_transform(X) 
#data.iloc[:, [0, 1, 2, 3, 4, 5, 6]]
predicted_data = pd.DataFrame(scaled_data).to_csv("test_3.csv", header = False, index = False)
print(scaled_data)
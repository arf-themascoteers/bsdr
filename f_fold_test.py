import pandas as pd
from sklearn import model_selection
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import KFold

x = np.random.rand(12, 7)
y = np.random.rand(12)

kf = KFold(n_splits=3)
for i, (train_index, test_index) in enumerate(kf.split(x)):
    print(train_index, test_index)


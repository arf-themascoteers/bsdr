import pandas as pd
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math
import numpy as np

regression = True

fulldata = pd.read_csv("data/lucas_skipped_min.csv").to_numpy()
X = fulldata[:,1:]
y = fulldata[:,0]

m1s = []
m2s = []
for i in range(10):
    train_x, test_x, train_y, test_y = model_selection.train_test_split(X,y, test_size=0.1, shuffle=True)
    model = SVC(C=1e5, kernel='rbf', gamma=1.)
    if regression:
        model = SVR(C=100, kernel='rbf', gamma=1.)
    model.fit(train_x, train_y)
    y_pred = model.predict(test_x)
    if not regression:
        y_pred = np.argmax(y_pred, axis=1)
        m1 = accuracy_score(test_y, y_pred)
        m2 = cohen_kappa_score(test_y, y_pred)
    else:
        m1 = r2_score(test_y, y_pred)
        m2 = math.sqrt(mean_squared_error(test_y, y_pred))
    print(m1, m2)
    m1s.append(m1)
    m2s.append(m2)

print(sum(m1s)/len(m1s))
print(sum(m2s)/len(m2s))



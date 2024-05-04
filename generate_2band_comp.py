from sklearn.svm import SVR
import pandas as pd
from ds_manager import DSManager

lucas = DSManager(name="lucas_downsampled")

train_data, test_data = lucas.get_train_test()
train_x = train_data[:,0:-1]
train_y = train_data[:,-1]

test_x = test_data[:,0:-1]
test_y = test_data[:,-1]

df = pd.DataFrame(columns=["band1","band2","score"])

for i in range(train_x.shape[1]):
    for j in range(i, train_x.shape[1],1):
        model = SVR(C=100, kernel='rbf', gamma=1.)
        train_x_short = train_x[:,[i,j]]
        test_x_short = test_x[:,[i,j]]
        model.fit(train_x_short, train_y)
        score = model.score(test_x_short, test_y)
        row = {"band1":i+1, "band2": j+1, "score" :score}
        print(row)
        df.loc[len(df)] = row

df.to_csv("b2.csv", index=False)
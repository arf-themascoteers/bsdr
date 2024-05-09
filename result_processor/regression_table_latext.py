import pandas as pd

time_df = pd.read_csv("../final_results/regression_time.csv")
r2_df = pd.read_csv("../final_results/regression_r2.csv")
rmse_df = pd.read_csv("../final_results/regression_rmse.csv")

priority_order = ['PCA-loading', 'LASSO', 'MCUVE',
                  #'SPA',
                  'BS-Net-FC', 'BSDR','All Bands']
# r2_df['algorithm'] = pd.Categorical(r2_df['algorithm'], categories=priority_order, ordered=True)
# r2_df = r2_df.sort_values('algorithm')
print(r2_df)
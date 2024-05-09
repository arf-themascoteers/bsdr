import pandas as pd


def create_latex_table(metric):
    head = r"""
\begin{table}[H]
\caption{Details of the datasets used in this study.\label{reg_r2}}
%\newcolumntype{C}{>{\centering\arraybackslash}X}
\begin{tabularx}{\textwidth}{Lrrrrrr}
\toprule
\multicolumn{1}{c}{\textbf{}} & \multicolumn{6}{c}{\textbf{Target Size}} \\
\cline{2-7}
\multicolumn{1}{c}{\textbf{Algorithm}} & \textbf{5} & \textbf{10} & \textbf{15} & \textbf{20} & \textbf{25} & \textbf{30}\\
\midrule
            """

    tail = r"""\end{tabularx}
    \noindent{\footnotesize{}}
    \end{table}"""

    time_df = pd.read_csv("../final_results/regression_time.csv")
    r2_df = pd.read_csv("../final_results/regression_r2.csv")
    rmse_df = pd.read_csv("../final_results/regression_rmse.csv")
    
    priority_order = ['PCAL', 'LASSO', 'MCUVE','SPA','BS-Net-FC', 'BSDR','All Bands']
    
    time_df['algorithm'] = pd.Categorical(time_df['algorithm'], categories=priority_order, ordered=True)
    time_df = time_df.sort_values('algorithm')

    r2_df['algorithm'] = pd.Categorical(r2_df['algorithm'], categories=priority_order, ordered=True)
    r2_df = r2_df.sort_values('algorithm')

    rmse_df['algorithm'] = pd.Categorical(rmse_df['algorithm'], categories=priority_order, ordered=True)
    rmse_df = rmse_df.sort_values('algorithm')

    keys = ['time', 'r2', 'rmse']
    dfs = [time_df, r2_df, rmse_df]
    index = keys.index(metric)

    targets_size = [5, 10, 15, 20, 25, 30]
    mid = ""

    base_df = dfs[index]
    for algorithm in priority_order:
        if metric == "time" and algorithm == "All Bands":
            continue
        df = base_df[base_df['algorithm'] == algorithm]
        row = df.iloc[0]
        mid = mid + f"{algorithm} "
        for t in targets_size:
            key = f"{metric}_{t}"
            mid = mid + f"& {row[key]} "
        mid = mid + r"\\ " + "\n"
    mid = mid + r"\bottomrule " +"\n"

    print(head + mid + tail)

create_latex_table("time")
import pandas as pd


def create_latex_table(metric, dataset):
    head = r"""
\begin{table}[H]
\caption{$R^2$ based on 10-fold cross validation results for different target sizes on LUCAS dataset. BSDR outperforms other algorithms with a consistent standard deviation.\label{reg_r2}}
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

    time_df = pd.read_csv(f"../final_results/{dataset}_time.csv")
    r2_df = pd.read_csv(f"../final_results/{dataset}_r2.csv")
    rmse_df = pd.read_csv(f"../final_results/{dataset}_rmse.csv")

    priority_order = ['MCUVE', 'SPA', 'BS-Net-FC', 'Zhang et al.', 'BSDR', 'All Bands']

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
        if algorithm == "All Bands":
            continue
        if metric == "time" and algorithm == "All Bands":
            continue
        df = base_df[base_df['algorithm'] == algorithm]
        if len(df) == 0:
            continue
        row = df.iloc[0]

        if algorithm == "All Bands":
            mid = mid + algorithm + r" & \multicolumn{6}{c}{" + row[f"{metric}_{targets_size[0]}"] + r"} \\" + "\n"
        else:
            mid = mid + f"{algorithm} "
            for t in targets_size:
                key = f"{metric}_{t}"
                mid = mid + f"& {row[key]} "
            mid = mid + r"\\ " + "\n"
    mid = mid + r"\bottomrule " + "\n"

    print(head + mid + tail)


create_latex_table("r2", "LUCAS")


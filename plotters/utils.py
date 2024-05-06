dataset_map = {
    "lucas_full":"LUCAS",
    "lucas_skipped":"LUCAS (Skipped)",
    "lucas_downsampled":"LUCAS (Downsampled)",
    "lucas_min":"LUCAS (Truncated)",
    "indian_pines":"Indian Pines",
    "ghsi":"GHISA",
}

metric_map = {
    "time":{
        "LUCAS": "Logarithmic Execution Time",
        "LUCAS (Skipped)": "Logarithmic Execution Time",
        "LUCAS (Downsampled)": "Logarithmic Execution Time",
        "LUCAS (Truncated)": "Logarithmic Execution Time",
        "Indian Pines": "Logarithmic Execution Time",
        "GHISA": "Logarithmic Execution Time",
    },
    "metric1":{
        "LUCAS": "$R^2$",
        "LUCAS (Skipped)": "$R^2$",
        "LUCAS (Downsampled)": "$R^2$",
        "LUCAS (Truncated)": "$R^2$",
        "Indian Pines": "Overall Accuracy",
        "GHISA": "Overall Accuracy",
    },
    "metric2":{
        "LUCAS": "$RMSE$",
        "LUCAS (Skipped)": "$RMSE$",
        "LUCAS (Downsampled)": "$RMSE$",
        "LUCAS (Truncated)": "$RMSE$",
        "Indian Pines": "Cohen's Kappa",
        "GHISA": "Cohen's Kappa",
    }
}

algorithm_map = {
    "all_bands" : "All Bands",
    "bsdr":"BSDR",
    "bsnet":"BS-Net-FC",
    "zhang":"Zhang et al.",
    "mcuve":"MCUVE",
    "pcal":"PCA-loading",
    "lasso":"LASSO",
    "spa":"SPA",
}

color_map = {
    "All Bands" : "black",
    "BSDR":"blue",
    "BS-Net-FC":"red",
    "Zhang et al.":"green",
    "MCUVE":"purple",
    "PCA-loading":"brown",
    "LASSO":"pink",
    "SPA":"cyan",
}


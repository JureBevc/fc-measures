from measures import pearson, covariance, mutual_information, partial_correlation, icov, cross_correlation, transfer_entropy, coherence
import numpy as np
import pandas as pd
import neurolib
from neurolib.models.aln import ALNModel
from neurolib.utils.loadData import Dataset
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time
import json

plot_df = pd.DataFrame()
signal_counts = [i for i in range(1000, 10000, 1000)]
plot_df["Signal count"] = signal_counts
SIGNAL_LENGTH = 100

methods = {
    "Pearsonov koeficient": pearson.pearson,
    "Vzajemna informacija": mutual_information.mutual_information,
    "Inverzna kovarianca": icov.ICOV,
    "Navzkrižna korelacija": cross_correlation.cross_correlation,
    "Entropija prenosa": transfer_entropy.transfer_entropy,
    "Koherenca": coherence.coherence
}


def saved_mean(method):
    b = []
    try:
        with open(method + " mean", "r") as fp:
            b = json.load(fp)
    except Exception as e:
        pass
    return b


def saved_std(method):
    b = []
    try:
        with open(method + " std", "r") as fp:
            b = json.load(fp)
    except Exception as e:
        pass
    return b


for method in methods:
    print(method)
    mean_results = saved_mean(method)
    std_results = saved_std(method)

    if mean_results == [] or std_results == []:
        for signal_count in signal_counts:
            if signal_count % 100 == 0:
                print(signal_count)
            input_array = np.random.rand(signal_count, SIGNAL_LENGTH)
            temp_results = []
            for i in range(10):
                start_time = time.time() * 1000
                pearson.pearson(input_array)
                end_time = time.time() * 1000
                temp_results.append(end_time - start_time)
            mean_results.append(np.mean(temp_results))
            std_results.append(np.std(temp_results))

    with open(method + " mean", "w") as fp:
        json.dump(mean_results, fp)

    with open(method + " std", "w") as fp:
        json.dump(std_results, fp)

    plot_df[method] = mean_results


fig = make_subplots(
    rows=4,
    cols=2,
    subplot_titles=plot_df.loc[:, plot_df.columns != "Signal count"].columns,
    x_title="Število signalov",
    y_title="Čas [ms]")
for i, column in enumerate(plot_df.loc[:, plot_df.columns != "Signal count"].columns):
    fig.add_trace(go.Scatter(x=plot_df["Signal count"], y=plot_df[column],
                             mode='lines',
                             name=column),
                  row=1 + i // 2,
                  col=1 + i % 2)
    #fig["layout"][f"xaxis{i}" if i > 0 else "xaxis"]["title"]= "σ"
    #fig["layout"][f"yaxis{i}"]["title"]= "Label X axis 2"
    fig["layout"][f"yaxis{i+1}"]["range"] = [0, 2500]

fig.update_layout(title_text="Dimension test",
                  font=dict(
                      size=11,
                  ))

# fig.update_layout(yaxis_title="Amplituda")
fig.update_layout(showlegend=False)
fig.show()

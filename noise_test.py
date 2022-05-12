from measures import pearson, covariance, mutual_information, partial_correlation, icov, cross_correlation, transfer_entropy, coherence
import numpy as np
import pandas as pd
import neurolib
from neurolib.models.aln import ALNModel
from neurolib.utils.loadData import Dataset
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

model = ALNModel()
model.params['sigma_ou'] = 0  # add some noise
model.params['duration'] = 2*1000  # milliseconds
model.run(bold=True)

original_signal = model.output[0][7000:]
noise_amounts = np.linspace(0, 30, 100)

print(len(original_signal))

plot_df = pd.DataFrame()
plot_df["Noise amount"] = noise_amounts

print("Pearson...")
# Pearson
pearson_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    pearson_results.append(pearson.pearson(np.array([original_signal, signal_noised]))[0][1])
plot_df["Pearsonov koeficient"] = pearson_results

print("Covariance...")
# Covariance
covariance_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    covariance_results.append(covariance.covariance(np.array([original_signal, signal_noised]))[0][1])
plot_df["Kovarianca"] = covariance_results

print("Mutual information...")
# Mutual information
mutual_information_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    mutual_information_results.append(mutual_information.mutual_information(np.array([original_signal, signal_noised]))[0][1])
plot_df["Vzajemna informacija"] = mutual_information_results

"""
print("Partial correlation...")
# Partial correlation
partial_correlation_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    signal_noised2 = original_signal + np.random.normal(0, np.sqrt(30), len(original_signal))
    partial_correlation_results.append(partial_correlation.partial_correlation(np.array([original_signal, signal_noised]),  [signal_noised2])[0][1])
plot_df["Partial correlation"] = partial_correlation_results
"""

print("ICOV...")
# ICOV
icov_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    icov_results.append(icov.ICOV(np.array([original_signal, signal_noised]))[0][1])
plot_df["Inverzna kovarianca"] = icov_results

print("Cross correlation...")
# Cross correlation
cross_correlation_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    cross_correlation_results.append(cross_correlation.cross_correlation(np.array([original_signal, signal_noised]))[0][1])
plot_df["Navzkrižna korelacija"] = cross_correlation_results

print("Transfer entropy...")
# Transfer entropy
transfer_entropy_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    input1 = np.digitize(original_signal, bins=[original_signal.mean()])
    input2 = np.digitize(signal_noised, bins=[signal_noised.mean()])
    transfer_entropy_results.append(transfer_entropy.transfer_entropy(np.array([input1, input2]))[0][1])
plot_df["Entropija prenosa"] = transfer_entropy_results

print("Coherence...")
# Coherence
coherence_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    coherence_results.append(coherence.coherence(np.array([original_signal, signal_noised]))[0][1])
plot_df["Koherenca"] = coherence_results

#plot_df = (plot_df - plot_df.mean())/plot_df.std()

fig = make_subplots(
    rows=4,
    cols=2,
    subplot_titles=plot_df.loc[:, plot_df.columns != "Noise amount"].columns,
    x_title="σ",
    y_title="Vrednost metrike")
for i, column in enumerate(plot_df.loc[:, plot_df.columns != "Noise amount"].columns):
    fig.add_trace(go.Scatter(x=plot_df["Noise amount"], y=plot_df[column],
                             mode='lines',
                             name=column),
                  row=1 + i // 2,
                  col=1 + i % 2)
    #fig["layout"][f"xaxis{i}" if i > 0 else "xaxis"]["title"]= "σ"
    #fig["layout"][f"yaxis{i}"]["title"]= "Label X axis 2"

fig.update_layout(title_text="Noise test",
                  font=dict(
                      size=11,
                  ))

# fig.update_layout(yaxis_title="Amplituda")
fig.show()

from measures import pearson, covariance, mutual_information, partial_correlation, icov, tangent, cross_correlation, transfer_entropy, coherence
import numpy as np
import pandas as pd
import neurolib
from neurolib.models.aln import ALNModel
from neurolib.utils.loadData import Dataset
import plotly.express as px
import plotly.graph_objs as go


model = ALNModel()
model.params['sigma_ou'] = 0  # add some noise
model.params['duration'] = 2*1000  # milliseconds
model.run(bold=True)

original_signal = model.output[0][7000:]
noise_amounts = np.linspace(0, 30, 100)

plot_df = pd.DataFrame()
plot_df["Noise amount"] = noise_amounts

print("Pearson...")
# Pearson
pearson_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    pearson_results.append(pearson.pearson(np.array([original_signal, signal_noised]))[0][1])
plot_df["Pearson"] = pearson_results

print("Covariance...")
# Covariance
covariance_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    covariance_results.append(covariance.covariance(np.array([original_signal, signal_noised]))[0][1])
plot_df["Covariance"] = covariance_results

print("Mutual information...")
# Mutual information
mutual_information_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    mutual_information_results.append(mutual_information.mutual_information(np.array([original_signal, signal_noised]))[0][1])
plot_df["Mutual information"] = mutual_information_results

print("Partial correlation...")
# Partial correlation
partial_correlation_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    partial_correlation_results.append(partial_correlation.partial_correlation(np.array([original_signal, signal_noised]))[0][1])
plot_df["Partial correlation"] = partial_correlation_results

print("ICOV...")
# ICOV
icov_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    icov_results.append(icov.ICOV(np.array([original_signal, signal_noised]))[0][1])
plot_df["ICOV"] = icov_results

"""
print("Tangent...")
# Tangent
tangent_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    tangent_results.append(tangent.tangent(np.array([original_signal, signal_noised]))[0][1])
plot_df["Tangent"] = tangent_results
"""

print("Cross correlation...")
# Cross correlation
cross_correlation_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    cross_correlation_results.append(cross_correlation.cross_correlation(np.array([original_signal, signal_noised]))[0][1])
plot_df["Cross correlation"] = cross_correlation_results

print("Transfer entropy...")
# Transfer entropy
transfer_entropy_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    transfer_entropy_results.append(transfer_entropy.transfer_entropy(np.array([original_signal, signal_noised]))[0][1])
plot_df["Transfer entropy"] = transfer_entropy_results

print("Coherence...")
# Coherence
coherence_results = []
for noise_amount in noise_amounts:
    signal_noised = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    coherence_results.append(coherence.coherence(np.array([original_signal, signal_noised]))[0][1])
plot_df["Coherence"] = coherence_results

#plot_df = (plot_df - plot_df.mean())/plot_df.std()

fig = go.Figure()
for column in plot_df.columns:
    if column == "Noise amount":
        continue
    fig.add_trace(go.Scatter(x=plot_df["Noise amount"], y=plot_df[column],
                             mode='lines+markers',
                             name=column))

fig.show()

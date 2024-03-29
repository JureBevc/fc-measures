from measures import pearson, mutual_information, icov, cross_correlation, transfer_entropy, coherence
import numpy as np
import pandas as pd
from neurolib.models.aln import ALNModel
from neurolib.utils.loadData import Dataset
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

model = ALNModel()
model.params['sigma_ou'] = 0  # add some noise
model.params['duration'] = 2*1000  # milliseconds
model.run(bold=True)

original_signal = model.output[0]

"""
q75, q25 = np.percentile(original_signal, [75 ,25])
iqr = q75 - q25
print(iqr)
n3 = np.power(len(original_signal), 1/3)
h = 2 * iqr / n3
print(h)
print((max(original_signal) - min(original_signal)) / h)
exit()
"""

bin_values = np.linspace(min(original_signal), max(original_signal), 67)

shift_amounts = np.arange(0, 1500, step=10)


SIGNAL_MIN_INDEX = 7000
SIGNAL_MAX_INDEX = 17000
fig = px.line(pd.DataFrame(
    {"signal": original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]}))
# fig.update_layout(legend={"title_text":""})
fig.update_layout(showlegend=False)
fig.update_layout(xaxis_title="Vzorec")
fig.update_layout(yaxis_title="Amplituda")
fig.write_html("original_signal.html")

plot_df = pd.DataFrame()
plot_df["Shift amount"] = shift_amounts

print("Pearson...")
# Pearson
pearson_results = []
for shift_amount in shift_amounts:
    signal_shifted = np.roll(original_signal, shift_amount)[
        SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    pearson_results.append(pearson.pearson(np.array(
        [original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX], signal_shifted]))[0][1])
plot_df["Pearsonov koeficient"] = pearson_results

"""
print("Covariance...")
# Covariance
covariance_results = []
for shift_amount in shift_amounts:
    signal_shifted = np.roll(original_signal, shift_amount)[
        SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    covariance_results.append(covariance.covariance(np.array(
        [original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX], signal_shifted]))[0][1])
plot_df["Kovarianca"] = covariance_results
"""

print("Mutual information...")
# Mutual information
mutual_information_results = []
for shift_amount in shift_amounts:
    signal_shifted = np.roll(original_signal, shift_amount)[
        SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    org_sig = original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    input1 = np.digitize(org_sig, bins=bin_values)
    input2 = np.digitize(signal_shifted, bins=bin_values)
    mutual_information_results.append(mutual_information.mutual_information(np.array(
        [input1, input2]))[0][1])
plot_df["Vzajemna informacija"] = mutual_information_results

"""
print("Partial correlation...")
# Partial correlation
partial_correlation_results = []
for shift_amount in shift_amounts:
    signal_shifted = np.roll(original_signal, shift_amount)[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    partial_correlation_results.append(partial_correlation.partial_correlation(np.array([original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX], signal_shifted]))[0][1])
plot_df["Partial correlation"] = partial_correlation_results
"""

print("ICOV...")
# ICOV
icov_results = []
for shift_amount in shift_amounts:
    signal_shifted = np.roll(original_signal, shift_amount)[
        SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    icov_results.append(icov.ICOV(np.array(
        [original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX], signal_shifted]))[0][1])
plot_df["Inverzna kovarianca"] = icov_results

"""
print("Tangent...")
# Tangent
tangent_results = []
for noise_amount in noise_amounts:
    signal_shifted = original_signal + np.random.normal(0, np.sqrt(noise_amount), len(original_signal))
    tangent_results.append(tangent.tangent(np.array([original_signal, signal_shifted]))[0][1])
plot_df["Tangent"] = tangent_results
"""

print("Cross correlation...")
# Cross correlation
cross_correlation_results = []
for shift_amount in shift_amounts:
    signal_shifted = np.roll(original_signal, shift_amount)[
        SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    cross_correlation_results.append(cross_correlation.cross_correlation(np.array(
        [original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX], signal_shifted]))[0][1])
plot_df["Navzkrižna korelacija"] = cross_correlation_results


print("Transfer entropy...")
# Transfer entropy
transfer_entropy_results = []
for shift_amount in shift_amounts:
    org_sig = original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    signal_shifted = np.roll(org_sig, shift_amount)
    input1 = np.digitize(org_sig, bins=[org_sig.mean()])
    input2 = np.digitize(signal_shifted, bins=[signal_shifted.mean()])
    transfer_entropy_results.append(
        transfer_entropy.transfer_entropy(np.array([input1, input2]))[0][1])
plot_df["Entropija prenosa"] = transfer_entropy_results

print("Coherence...")
# Coherence
coherence_results = []
for shift_amount in shift_amounts:
    signal_shifted = np.roll(original_signal, shift_amount)[
        SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX]
    coherence_results.append(coherence.coherence(np.array(
        [original_signal[SIGNAL_MIN_INDEX:SIGNAL_MAX_INDEX], signal_shifted]))[0][1])
plot_df["Koherenca"] = coherence_results

#plot_df = (plot_df - plot_df.mean())/plot_df.std()

fig = make_subplots(
    rows=3,
    cols=2,
    subplot_titles=plot_df.loc[:, plot_df.columns != "Shift amount"].columns,
    x_title="δ",
    y_title="Vrednost metrike")
for i, column in enumerate(plot_df.loc[:, plot_df.columns != "Shift amount"].columns):
    fig.add_trace(go.Scatter(x=plot_df["Shift amount"], y=plot_df[column],
                             mode='lines',
                             name=column),
                  row=1 + i // 2,
                  col=1 + i % 2)

    if column not in ["Koherenca", "Entropija prenosa", "Vzajemna informacija"]:
        fig["layout"][f"yaxis{i+1}"]["range"] = [-1, 1]
    else:
        print(column)
        fig["layout"][f"yaxis{i+1}"]["range"] = [0, 1]

fig.update_layout(title_text='Shift test',
                  font=dict(
                      size=11,
                  ))
fig.show()

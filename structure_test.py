from measures import pearson, mutual_information, icov, cross_correlation, transfer_entropy, coherence
import numpy as np
import pandas as pd
import neurolib
from neurolib.models.aln import ALNModel
from neurolib.utils.loadData import Dataset
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import seaborn as sns
import plotly.figure_factory as ff

SIGNAL_LENGTH = 1000
A_original = np.random.rand(SIGNAL_LENGTH)
B_original = np.random.rand(SIGNAL_LENGTH)
C_original = np.random.rand(SIGNAL_LENGTH)

bin_values = np.linspace(0, 1, 12)
methods = [
    pearson.pearson,
    mutual_information.mutual_information,
    icov.ICOV,
    cross_correlation.cross_correlation,
    transfer_entropy.transfer_entropy,
    coherence.coherence
]

fig = make_subplots(rows=3, cols=2, 
subplot_titles=(
    "Pearsonov koeficient",
    "Vzajemna informacija", 
    "Inverzna kovarianca",
    "Navzkrižna korelacija",
    "Entropija prenosa",
    "Koherenca",
    )
)
print("---")
print("Case B <- A -> C")
for i, method in enumerate(methods):
    A = A_original.copy()
    B = B_original.copy()
    C = C_original.copy()
    input1 = A
    input2 = (A + B) / 2
    input3 = (A + C) / 2

    if i == 1:
        A = np.digitize(A, bins=bin_values)
        B = np.digitize(B, bins=bin_values)
        C = np.digitize(C, bins=bin_values)
        input1 = np.digitize(input1, bins=bin_values)
        input2 = np.digitize(input2, bins=bin_values)
        input3 = np.digitize(input3, bins=bin_values)

    elif i == 4:
        A = np.digitize(A, bins=[np.mean(A)])
        B = np.digitize(B, bins=[np.mean(B)])
        C = np.digitize(C, bins=[np.mean(C)])
        input1 = np.digitize(input1, bins=[np.mean(input1)])
        input2 = np.digitize(input2, bins=[np.mean(input2)])
        input3 = np.digitize(input3, bins=[np.mean(input3)])

    original_res = method(np.array([A, B, C]))
    new_res = method(np.array([input1, input2, input3]))
    text_format = [[ f"{m:.2f}" for m in n ] for n in new_res]
    fig.add_trace(go.Heatmap(z=new_res, coloraxis = "coloraxis",
                x=['A', 'B', 'C'],
                y=['A', 'B', 'C'],
                text=text_format,
                texttemplate="%{text}",
                textfont={"size":10},), col=1 + i%2, row=1 + i//2)
    print(f"{method.__name__}")
    print(f"{original_res[0][1]:0.2f}")
    print(f"{new_res[0][1]:0.2f}")

fig.update_layout(coloraxis = {'colorscale':'RdBu'},)
fig.show()


fig = make_subplots(rows=3, cols=2, 
subplot_titles=(
    "Pearsonov koeficient",
    "Vzajemna informacija", 
    "Inverzna kovarianca",
    "Navzkrižna korelacija",
    "Entropija prenosa",
    "Koherenca",
    )
)
print("---")
print("Case A -> B -> C")
for i, method in enumerate(methods):
    A = A_original.copy()
    B = B_original.copy()
    C = C_original.copy()
    input1 = A
    input2 = (A + B) / 2
    input3 = (input2 + C) / 2

    if i == 1:
        A = np.digitize(A, bins=bin_values)
        B = np.digitize(B, bins=bin_values)
        C = np.digitize(C, bins=bin_values)
        input1 = np.digitize(input1, bins=bin_values)
        input2 = np.digitize(input2, bins=bin_values)
        input3 = np.digitize(input3, bins=bin_values)

    elif i == 4:
        A = np.digitize(A, bins=[np.mean(A)])
        B = np.digitize(B, bins=[np.mean(B)])
        C = np.digitize(C, bins=[np.mean(C)])
        input1 = np.digitize(input1, bins=[np.mean(input1)])
        input2 = np.digitize(input2, bins=[np.mean(input2)])
        input3 = np.digitize(input3, bins=[np.mean(input3)])

    original_res = method(np.array([A, B, C]))
    new_res = method(np.array([input1, input2, input3]))
    text_format = [[ f"{m:.2f}" for m in n ] for n in new_res]
    fig.add_trace(go.Heatmap(z=new_res, coloraxis = "coloraxis",
                x=['A', 'B', 'C'],
                y=['A', 'B', 'C'],
                text=text_format,
                texttemplate="%{text}",
                textfont={"size":10},), col=1 + i%2, row=1 + i//2)

    print(f"{method.__name__}")
    print(f"{original_res[0][1]:0.2f}")
    print(f"{new_res[0][1]:0.2f}")

fig.update_layout(coloraxis = {'colorscale':'RdBu'},)
fig.show()

fig = make_subplots(rows=3, cols=2, 
subplot_titles=(
    "Pearsonov koeficient",
    "Vzajemna informacija", 
    "Inverzna kovarianca",
    "Navzkrižna korelacija",
    "Entropija prenosa",
    "Koherenca",
    )
)
# Case A -> C <- B
print("---")
print("Case A -> C <- B")
for i, method in enumerate(methods):
    A = A_original.copy()
    B = B_original.copy()
    C = C_original.copy()
    input1 = A
    input2 = B
    input3 = (A + B + C) / 3

    if i == 1:
        A = np.digitize(A, bins=bin_values)
        B = np.digitize(B, bins=bin_values)
        C = np.digitize(C, bins=bin_values)
        input1 = np.digitize(input1, bins=bin_values)
        input2 = np.digitize(input2, bins=bin_values)
        input3 = np.digitize(input3, bins=bin_values)

    elif i == 4:
        A = np.digitize(A, bins=[np.mean(A)])
        B = np.digitize(B, bins=[np.mean(B)])
        C = np.digitize(C, bins=[np.mean(C)])
        input1 = np.digitize(input1, bins=[np.mean(input1)])
        input2 = np.digitize(input2, bins=[np.mean(input2)])
        input3 = np.digitize(input3, bins=[np.mean(input3)])

    original_res = method(np.array([A, B, C]))
    new_res = method(np.array([input1, input2, input3]))
    text_format = [[ f"{m:.2f}" for m in n ] for n in new_res]
    fig.add_trace(go.Heatmap(z=new_res, coloraxis = "coloraxis",
                x=['A', 'B', 'C'],
                y=['A', 'B', 'C'],
                text=text_format,
                texttemplate="%{text}",
                textfont={"size":10},), col=1 + i%2, row=1 + i//2)

    print(f"{method.__name__}")
    print(f"{original_res[0][1]:0.2f}")
    print(f"{new_res[0][1]:0.2f}")
fig.update_layout(coloraxis = {'colorscale':'RdBu'},)
fig.show()
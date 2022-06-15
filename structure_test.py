import enum
from re import I
from measures import pearson, mutual_information, icov, cross_correlation, transfer_entropy, coherence
import numpy as np
import pandas as pd
import neurolib
from neurolib.models.aln import ALNModel
from neurolib.utils.loadData import Dataset
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

SIGNAL_LENGTH = 1000
A_original = np.random.rand(SIGNAL_LENGTH)
B_original = np.random.rand(SIGNAL_LENGTH)
C_original = np.random.rand(SIGNAL_LENGTH)

methods = [
    pearson.pearson,
    mutual_information.mutual_information,
    icov.ICOV,
    cross_correlation.cross_correlation,
    transfer_entropy.transfer_entropy,
    coherence.coherence
]

print("---")
print("Case B <- A -> C")
for i, method in enumerate(methods):
    A = A_original.copy()
    B = B_original.copy()
    C = C_original.copy()
    input1 = A
    input2 = (A + B) / 2
    input3 = (A + C) / 2

    if i == 1 or i == 4:
        A = np.digitize(A, bins=[np.mean(A)])
        B = np.digitize(B, bins=[np.mean(B)])
        C = np.digitize(C, bins=[np.mean(C)])
        input1 = np.digitize(input1, bins=[np.mean(input1)])
        input2 = np.digitize(input2, bins=[np.mean(input2)])
        input3 = np.digitize(input3, bins=[np.mean(input3)])

    original_res = method(np.array([B, C, A]))
    new_res = method(np.array([input2, input3, input1]))

    print(f"{method.__name__}")
    print(f"{original_res[0][1]:0.2f}")
    print(f"{new_res[0][1]:0.2f}")

print("---")
print("Case A -> B -> C")
for i, method in enumerate(methods):
    A = A_original.copy()
    B = B_original.copy()
    C = C_original.copy()
    input1 = A
    input2 = (A + B) / 2
    input3 = (input2 + C) / 2

    if i == 1 or i == 4:
        A = np.digitize(A, bins=[np.mean(A)])
        B = np.digitize(B, bins=[np.mean(B)])
        C = np.digitize(C, bins=[np.mean(C)])
        input1 = np.digitize(input1, bins=[np.mean(input1)])
        input2 = np.digitize(input2, bins=[np.mean(input2)])
        input3 = np.digitize(input3, bins=[np.mean(input3)])

    original_res = method(np.array([A, C, B]))
    new_res = method(np.array([input1, input3, input2]))

    print(f"{method.__name__}")
    print(f"{original_res[0][1]:0.2f}")
    print(f"{new_res[0][1]:0.2f}")

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

    if i == 1 or i == 4:
        A = np.digitize(A, bins=[np.mean(A)])
        B = np.digitize(B, bins=[np.mean(B)])
        C = np.digitize(C, bins=[np.mean(C)])
        input1 = np.digitize(input1, bins=[np.mean(input1)])
        input2 = np.digitize(input2, bins=[np.mean(input2)])
        input3 = np.digitize(input3, bins=[np.mean(input3)])

    original_res = method(np.array([A, B, C]))
    new_res = method(np.array([input1, input2, input3]))

    print(f"{method.__name__}")
    print(f"{original_res[0][1]:0.2f}")
    print(f"{new_res[0][1]:0.2f}")

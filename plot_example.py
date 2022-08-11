import plotly.express as px
import plotly.graph_objs as go

new_res = [
    [1,0,0.5],
    [0,1,0.5],
    [0.5,0.5,1],
]

no_text = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

fig = go.Figure()
fig.add_trace(go.Heatmap(z=new_res, coloraxis = "coloraxis",
            x=['A', 'B', 'C'],
            y=['A', 'B', 'C'],
            text=no_text,))

fig.update_layout(coloraxis = {'colorscale':'RdBu', "cmax": 1, "cmin": -1},)
fig.show()
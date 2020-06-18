import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
# Traces
trace_1 = go.Bar(
    x=["西南石油", "东方明珠", "海泰发展"],
    y=[4.12, 5.32, 0.60],
    name="201609"
)


trace = [trace_1]
# Layout
layout = go.Layout(
    title='净资产收益率对比图'
)
# Figure
figure = go.Figure(data=trace, layout=layout)
# Plot
pyplt(figure, filename='2.html')
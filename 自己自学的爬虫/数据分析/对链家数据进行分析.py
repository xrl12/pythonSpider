import plotly as py
import plotly.graph_objs as go

with open('链家数据的.csv','rb') as f:
    f.seek(10,0)
    data = f.readlines().

    print(data)
    f.close()

# pyplt = py.offline.plot
# # Traces
# trace_1 = go.Bar(
#     x=["西南石油", "东方明珠", "海泰发展"],
#     y=[4.12, 5.32, 0.60],
#     name="201609"
# )
# layout = go.Layout(
#     title='净资产收益率对比图'
# )
# # Figure
# figure = go.Figure(data=trace_1, layout=layout)
# # Plot
# pyplt(figure, filename='2.html')

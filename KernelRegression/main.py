import numpy as np
import plotly.graph_objects as go
import plotly.express as px

tuning_param = 1

x_known = np.array([-4,-3.5,-2.5,-2,-0.5,0,1,1.5,2,2.5,4])
y_known = np.sin(x_known)

x_unknown = np.linspace(-5,5,100)
squared_distances = (np.repeat(x_unknown.reshape(-1,1),len(x_known),axis=1)-x_known)**2
kernel_values = np.exp(-0.5*squared_distances*tuning_param)
predictions = np.sum(kernel_values*y_known,axis=1)/np.sum(kernel_values,axis=1)

trace1 = go.Scatter(x=x_known, y=y_known, name="known points", mode="markers", showlegend=False,marker=dict(color="red",size=10))
trace2 = go.Scatter(x=x_unknown, y=predictions, name="unknown points", mode="lines", showlegend=False,line=dict(color="green",width=3))

layout = go.Layout(
	title = "Kernel Regression with tuning parameter:" + str(tuning_param),
	xaxis = dict(
		range=[-5.2,5.2],
		title = 'X',
		tickvals=np.arange(-5,6),
		zeroline = False,
		gridwidth = 2,
		tickangle=90,
		ticks="inside"
	),
	yaxis = dict(
		range=[-1.1,1.1],
		title = 'X',
		tickvals=[-1,-0.5,0,0.5,1],
		zeroline = False,
		gridwidth = 2,
		ticks="inside"
	),
	font=dict(size=16),
	showlegend=False,
	margin=dict(t=40,l=10,b=10,r=10),
	legend=dict(
    	orientation="v",
    	yanchor="top",
    	y=0.98,
    	xanchor="left",
    	x=0.02
	)
)

fig = go.Figure(data=[trace1,trace2],layout=layout)

fig.write_image("plot_data_pred.png",width=800,height=400)

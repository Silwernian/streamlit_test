import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import pandas as pd

m = st.slider('Slope, $m$',max_value=5,min_value=-5,step=1,value=1)
c = st.slider('Intercept, $c$',max_value=5,min_value=-5,step=1,value=0)

x = np.linspace(-10,10,100)
y = m*x+c

fig = go.Figure()
fig.add_trace(go.Scatter(x=x,y=y))
fig.update_layout(yaxis_range=[-10,10],xaxis_range=[-10,10])

st.plotly_chart(fig)

data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig2 = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value'
)
fig2.update_layout(
    template='plotly_dark'
)
st.plotly_chart(fig2,use_container_width=True)

z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

X = np.linspace(-50,50,200)
Y = np.linspace(-50,50,200)
y,x = np.meshgrid(X,Y)
z = x**2 - y**2


surface = go.Surface(x=x,y=y,z=z)

fig3 = go.Figure(surface)

fig3.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))

fig3.update_layout(template='plotly_dark',
                  title={'text':'Contour plot of a function from numpy'},
                  titlefont_size=30, titlefont_color='aqua')
st.plotly_chart(fig3, use_container_width=True)
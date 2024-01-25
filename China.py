# --Imports--
import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio

# Reading The Dataset
tdata = pd.read_csv('https://raw.githubusercontent.com/brendanmcc02/BMC-CCTE/master/tourismarrivals.csv')
cdata = pd.read_csv('https://raw.githubusercontent.com/brendanmcc02/BMC-CCTE/master/chinesetemp.csv')
crdata = pd.read_csv('https://raw.githubusercontent.com/brendanmcc02/BMC-CCTE/master/chineserain.csv')

# Cleaning The Dataset
cdata.rename(columns={' Statistics': 'Month', 'Temperature - (Celsius)': 'Temperature', ' Year': 'Year', ' Country': 'Country', ' ISO3': 'Code'}, inplace=True)
crdata.rename(columns={' Statistics': 'Month', 'Rainfall - (MM)': 'Rainfall', ' Year': 'Year', ' Country': 'Country', ' ISO3': 'Code'}, inplace=True)

cdata = cdata.query("Year != '1991'").query("Year != '1992'").query("Year != '1993'").query("Year != '1994'").query("Country != 'China'").query("Code != 'CHN'")
crdata = crdata.query("Year != '1991'").query("Year != '1992'").query("Year != '1993'").query("Year != '1994'").query("Country != 'China'").query("Code != 'CHN'")
tdata = tdata.query("Year != '2017'")

# Initialising Average Temperatures of Each Year
year = 1995
avgyear = []
yearslist = []
while year <= 2016:
    temp  = cdata[cdata['Year'] == year]['Temperature'].sum() / len(cdata[cdata['Year'] == year])
    avgyear.append(temp)
    yearslist.append(year)
    year = year + 1

# Initialising Average Rainfall of Each Year
year_r = 1995
avgyear_r = []
yearslist_r = []
while year_r <= 2016:
    rainfall  = crdata[crdata['Year'] == year_r]['Rainfall'].sum() / len(crdata[crdata['Year'] == year_r]) / 10
    avgyear_r.append(rainfall)
    yearslist_r.append(year_r)
    year_r = year_r + 1

# Analysing And Plotting The Data
fig = go.Figure()

fig.add_trace(go.Scatter(
                         x = yearslist,
                         y = avgyear,
                         mode = 'lines+markers',
                         name = 'Average Temperature in China'
                         ))

fig.add_trace(go.Scatter(
                         x = tdata['Year'] ,
                         y = tdata['China'] / 10000000 ,
                         mode = 'lines+markers',
                         name = 'Tourism Arrivals in China',
                         line_shape='spline'
                         ))

fig.add_trace(go.Scatter(
                         x = yearslist_r,
                         y = avgyear_r ,
                         mode = 'lines+markers',
                         name = 'Average Rainfall in China',
                         line_shape='spline'
                         ))

# Configuring The Presentation Of The Graph
fig.update_layout(
                  title = {
                      'text' : "Tourism Arrivals in China correlated with National Temperature and Rainfall (1995 - 2016)",
                      'y' : 0.95,
                      'x' : 0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'
                      },
                    xaxis_title = "Time (Years)",
                    yaxis_title = "Tourism Arrivals (10 Millions) // Temperature (°C) // Rainfall (cm)",
                    font = dict(
                        family = "Corbel",
                        size = 17,
                        color = "#000000"
                  )
                  )

# Configuring The Axes
fig.update_xaxes(
    range=[1994, 2017],
    ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10,
    showline=True, linewidth=1, linecolor='black',
    mirror=True, showgrid=True, gridwidth=1, gridcolor='white',
    zeroline=True, zerolinewidth=1, zerolinecolor='black')

fig.update_yaxes(
    range=[0, 10],
    ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10,
    showline=True, linewidth=1, linecolor='black',
    mirror=True, showgrid=True, gridwidth=1, gridcolor='white',
    zeroline=True, zerolinewidth=1, zerolinecolor='black')

# Display Graph
fig.show(renderer="browser")
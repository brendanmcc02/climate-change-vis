# --Imports--
import pandas as pd # Allows program to read CSV File
import plotly.graph_objects as go # Library for Graphs
import chart_studio.plotly as py # Allows program to upload graph to www.plot.ly
import chart_studio # Allows program to upload graph to www.plot.ly

# --Reading The Dataset--
tdata = pd.read_csv('https://raw.githubusercontent.com/brendanmcc02/BMC-CCTE/master/tourismarrivals.csv') # Reading Tourism Data
idata = pd.read_csv('https://raw.githubusercontent.com/brendanmcc02/BMC-CCTE/master/irishtemp.csv') # Reading Temperature Data
irdata = pd.read_csv('https://raw.githubusercontent.com/brendanmcc02/BMC-CCTE/master/irishrain.csv') # Reading Rainfall Data

# --Cleaning The Dataset--
idata.rename(columns={' Statistics': 'Month', 'Temperature - (Celsius)': 'Temperature', ' Year': 'Year', ' Country': 'Country', ' ISO3': 'Code'}, inplace=True) # Renaming Columns
irdata.rename(columns={' Statistics': 'Month', 'Rainfall - (MM)': 'Rainfall', ' Year': 'Year', ' Country': 'Country', ' ISO3': 'Code'}, inplace=True) # Renaming Columns

idata = idata.query("Year != '1991'").query("Year != '1992'").query("Year != '1993'").query("Year != '1994'").query("Country != 'Ireland'").query("Code != 'IRL'") # Excluding Unused Columns
irdata = irdata.query("Year != '1991'").query("Year != '1992'").query("Year != '1993'").query("Year != '1994'").query("Country != 'Ireland'").query("Code != 'IRL'") # Excluding Unused Columns 
tdata = tdata.query("Year != '2017'") # Excluding Unused Columns

# --Averaging 12 Months into 1 Year (Temperature)--
year_i = 1995 # Initialising variable
avgyear_i = [] # Creating empty list
yearslist_i = [] # Creating empty list
while year_i <= 2016:
    temp  = idata[idata['Year'] == year_i]['Temperature'].sum() / len(idata[idata['Year'] == year_i]) # Summing temperatures to find annual averages
    avgyear_i.append(temp) # Append years to the empty list
    yearslist_i.append(year_i) # Append years to the empty list
    year_i = year_i + 1 # Repeat until statement breaks

# --Averaging 12 Months into 1 Year (Rainfall)--
year_r = 1995 # Initialising variable
avgyear_r = [] # Creating empty list
yearslist_r = [] # Creating empty list
while year_r <= 2016:
    rainfall  = irdata[irdata['Year'] == year_r]['Rainfall'].sum() / len(irdata[irdata['Year'] == year_r]) / 10 # Summing rainfall to find annual averages, and converting from mm to cm
    avgyear_r.append(rainfall) # Append years to the empty list
    yearslist_r.append(year_r) # Append years to the empty list
    year_r = year_r + 1 # Repeat until statement breaks

# --Analysing And Plotting The Data--
fig = go.Figure()

fig.add_trace(go.Scatter( # Adding Plot for Temperature
                         x = yearslist_i, # x-axis Data
                         y = avgyear_i, # y-axis Data
                         mode = 'lines+markers', # Line Style
                         name = 'Average Temperature in Ireland' # Legend Name
                         ))

fig.add_trace(go.Scatter( # Adding Plot for Tourism
                         x = tdata['Year'] ,  # x-axis Data
                         y = tdata['Ireland'] / 1000000 ,  # y-axis Data, converting Millions to double digits
                         mode = 'lines+markers', # Line Style
                         name = 'Tourism Arrivals in Ireland', # Legend Label
                         line_shape='spline' # Line Shape
                         ))

fig.add_trace(go.Scatter( # Adding Plot for Rainfall
                         x = yearslist_r,  # x-axis Data
                         y = avgyear_r ,  # y-axis Data
                         mode = 'lines+markers', # Line Style
                         name = 'Average Rainfall in Ireland', # Legend Label
                         line_shape='spline' # Line Shape
                         ))

# --Configuring The Presentation Of The Graph--
fig.update_layout(
                  title = {
                      'text' : "Tourism Arrivals in Ireland correlated with National Temperature and Rainfall (1995 - 2016)", # Title
                      'y' : 0.95, # Positioning
                      'x' : 0.5, # Positioning
                      'xanchor': 'center', # Positioning
                      'yanchor': 'top' # Positioning
                      },
                    xaxis_title = "Time (Years)", # x-axis Label
                    yaxis_title = "Tourism Arrivals (Millions) // Temperature (°C) // Rainfall (cm)", # y-axis Label
                    font = dict( # Changing Font and Font Size
                        family = "Corbel",
                        size = 17,
                        color = "#000000"
                  )
                  )

# --Configuring The Axes--
fig.update_xaxes(
    range=[1994, 2017], # Customizing y-axis Range 
    ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, # Adding red ticks to the axes
    showline=True, linewidth=1, linecolor='black', # Changing Line Width and Colour
    mirror=True, showgrid=True, gridwidth=1, gridcolor='white', # Changing Grid-Line Width and Colour
    zeroline=True, zerolinewidth=1, zerolinecolor='black') # Changing Zero-Line Width and Colour

fig.update_yaxes(
    range=[0, 12], # Customizing y-axis Range
    ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, # Adding red ticks to the axes
    showline=True, linewidth=1, linecolor='black', # Changing Line Width and Colour
    mirror=True, showgrid=True, gridwidth=1, gridcolor='white', # Changing Grid-Line Width and Colour
    zeroline=True, zerolinewidth=1, zerolinecolor='black') # Changing Zero-Line Width and Colour

# Display Graph
fig.show(renderer="browser") # Displays Graph in Browser
# Here we have a list of Dictionaries for the weather readings in Salalah City
Salalah_Forecast = [
    {'humidity':  20, 'temperature': 78, 'wind':  7},
    {'humidity':  50, 'temperature': 61, 'wind': 10},
    {'humidity': 100, 'temperature': 81, 'wind':  5},
    {'humidity':  90, 'temperature': 62, 'wind': 15},
    {'humidity':  30, 'temperature': 84, 'wind': 19},
    {'humidity':   0, 'temperature': 66, 'wind': 28},
    {'humidity':   0, 'temperature': 87, 'wind': 12},
    {'humidity':   0, 'temperature': 68, 'wind': 14},
    {'humidity':   0, 'temperature': 86, 'wind':  4},
    {'humidity':  60, 'temperature': 68, 'wind':  0}
]

# For example to get the wind volicity we use the following loop
for forecast in Salalah_Forecast:
    wind_speed = forecast['wind']
    print(wind_speed)

# In our Template we can use something like

<ul >
{ % for w in wind_speed % }
<li >
wind speed = {{w.wind}}

{ % endfor % }
</ul >

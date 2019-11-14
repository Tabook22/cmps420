# here we have a forecase data

forecast = {'sal_data': [{'humidity':  20, 'temperature': 78, 'wind':  7},
                         {'humidity':  50, 'temperature': 61, 'wind': 10},
                         {'humidity': 100, 'temperature': 81, 'wind':  5},
                         {'humidity':  90, 'temperature': 62, 'wind': 15},
                         {'humidity':  30, 'temperature': 84, 'wind': 19},
                         {'humidity':   0, 'temperature': 66, 'wind': 28},
                         {'humidity':   0, 'temperature': 87, 'wind': 12},
                         {'humidity':   0, 'temperature': 68, 'wind': 14},
                         {'humidity':   0, 'temperature': 86, 'wind':  4},
                         {'humidity':  60, 'temperature': 68, 'wind':  0}
                         ]}

# in the views.py
# -------------------


def salalah_data():
    # here we can selecting which key to work with
    cat = input("enter variable:   ")
    w_data = forecast['sal_data']

    # or we can use it in our templates
    return render(request, "forecast.html", {'weather': w_data})


# in the template forecast.html
# ------------------------
<table >
<tr >
<td >  # </td><td>Humidity</td><td>Temperature</td><td>wind</td>
</tr >
{ % for w in weather%}
   <tr >
        <td > {{forloop.counter}} < /td >
        <td > {{w.humidity}} < /td >
        <td > {{w.temperature}} < /td >
        <td > {{w.wind}} < /td >
    </tr >
{ % endfor % }
</table >

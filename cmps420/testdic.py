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


def salalah_data():
    # here we selecting
    cat = input("enter variable:   ")
    sd = forecast['sal_data']
    for w in sd:
        print(w[cat])


if __name__ == "__main__":
    salalah_data()

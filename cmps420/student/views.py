from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "student/index.html")

# This function is used to check the request type


def check_request(request):
    if request.method == "POST":
        msg = "The request method is:  POST"
    else:
        msg = "The request method is:  GET"

    return render(request, "student/crq.html", {'ms': msg})


# This function is used to get the request of
# type post and then display the result back to the user
def show_result(request):
    msg = ""
    if request.method == "POST":
        msg = request.POST['name'] + " --- " + request.POST['col']

    return render(request, "student/showresult.html", {'ms': msg})


# Reading data from dictionary
def show_wind(request):
    forecast = [{'sal_data': {'humidity':  20, 'temperature': 78, 'wind':  7},
                 'sal_data': {'humidity':  50, 'temperature': 61, 'wind': 10},
                 'sal_data': {'humidity': 100, 'temperature': 81, 'wind':  5},
                 'sal_data': {'humidity':  90, 'temperature': 62, 'wind': 15},
                 'sal_data': {'humidity':  30, 'temperature': 84, 'wind': 19},
                 'sal_data': {'humidity':   0, 'temperature': 66, 'wind': 28},
                 'sal_data': {'humidity':   0, 'temperature': 87, 'wind': 12},
                 'sal_data': {'humidity':   0, 'temperature': 68, 'wind': 14},
                 'sal_data': {'humidity':   0, 'temperature': 86, 'wind':  4},
                 'sal_data': {'humidity':  60, 'temperature': 68, 'wind':  0}
                 }]

    for salalah_data in forecast:
        sal_wind = salalah_data
        print(sal_wind)

    return render(request, "student/show_wind.html", {'wd': sal_wind})

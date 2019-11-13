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

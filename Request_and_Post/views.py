from django.shortcuts import render

def check_request(request):
    msg=""
    if request.method =="POST":
        msg="This request Method is POST"
    else:
        msg="This request Method is GET"

    return render(request,"request.html",{'ms':msg})



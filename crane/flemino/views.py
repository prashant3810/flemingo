from django.http import HttpResponse
def show(request):
    return HttpResponse ("I am in show view")

def sai(request):
    return HttpResponse("I am in Bangalore")

def abc(request):
    return HttpResponse("rserve world")

def duke(request):
    return HttpResponse(" damn good performance")
def dude(request):
    return HttpResponse(" i am in flair \n"
                        "hardwork neverpaysoff \n"
                        "life is too logical ")


# Create your views here.

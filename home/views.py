from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Deployment Ready Django Project</h1>")

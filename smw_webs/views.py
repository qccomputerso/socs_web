from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'smw_webs/index.html')
def events(request):
    return render(request, 'smw_webs/events.html')
def contact(request):
    return render(request, 'smw_webs/contact.html')
def oday(request):
    return render(request, 'smw_webs/oday.html')
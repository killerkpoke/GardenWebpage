from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html')

def service(request):
    return render(request, 'polls/services.html')

def bag(request):
    return render(request, 'polls/bag.html')

def contact(request):
    return render(request, 'polls/contact.html')
def item(request):
    return render(request, 'polls/item.html')

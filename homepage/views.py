from django.shortcuts import render
from cases.models import Case

# Create your views here.

def index (request):

    return render (request, "homepage/index.html")

def malina(request):
    
    return render (request, "homepage/malina.html")

def premiot(request):

    if request.method == "POST":

        first_name = request.POST ['first-name']
        last_name = request.POST ['last-name']
        email = request.POST ['email']
        phone = request.POST ['phone']
        message = request.POST ['message']
        file01 = request.FILES.get('file_input_01')
        file02 = request.FILES.get('file_input_02')
        file03 = request.FILES.get('file_input_03')
    
        case = Case.objects.create()
        case.first_name = first_name
        case.last_name = last_name
        case.email = email
        case.phone = phone
        case.message = message
        case.file01 = file01
        case.file02 = file02
        case.file03 = file03

        case.save()

        return render (request, 'cases/success.html')

    return render (request, "homepage/premiot.html")
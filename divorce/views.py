from django.shortcuts import render
from .models import Divorce
from django.views.generic import CreateView
from divorce.models import Divorce

# Create your views here.
def form_1 (request):
    if request.method=="POST":
        name = request.POST['name']
        State_issued_divorce_id = request.POST['State_issued_divorce_id']
        Date_of_birth = request.POST['Date_of_birth']
        Nationality = request.POST['Nationality']
        Maritial_status = request.POST['Maritial_status']
        Highest_education = request.POST['Highest_education']
    
        divorce = Divorce(name=name, State_issued_divorce_id=State_issued_divorce_id, Date_of_birth=Date_of_birth,
        Nationality=Nationality,
        Maritial_status=Maritial_status,
        Highest_education=Highest_education )

        divorce.save()

    return render(request, "form_1.html")
# def form_2 (request):
#     return render(request, "form_2.html")
# def form_3 (request):
#     return render(request, "form_3.html")


# class Form_1(CreateView):
#     model = Divorce 
#     template_name = "form_1.html" 
#     fields = "name", "State_issued_divorce_id"
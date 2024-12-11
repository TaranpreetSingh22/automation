from django.shortcuts import render

# Create your views here.
def cse(request):
    return render(request, 'cseDept/cse.html')

def reqQuot(request):
    return render(request, 'cseDept/request_quotation.html')
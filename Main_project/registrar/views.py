from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registrar_dashboard(request):
    '''
    document_url = "/path/to/your/document.pdf"  # Replace with the actual document path or URL
    context = {
        "document_url": document_url
    }
   '''
    return render(request, "rg_dashboard.html")

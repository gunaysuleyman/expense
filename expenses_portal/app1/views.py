from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'app1/index.html')

def add_expense(request):

    
    return render(request, 'app1/add_expense.html')
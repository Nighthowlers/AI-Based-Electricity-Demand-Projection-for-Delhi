from django.shortcuts import render, redirect

def login(request):
    # Your login logic here
    # For example, let's assume you have a form in your 1.html template
    # and you want to redirect to the Predictor view after the form is submitted
    if request.method == 'POST':
        # Your form validation and login logic here
        return redirect('Predictor')
    else:
        return render(request, "1.html")

def Predictor(request):
    return render(request, "Predictor.html")

def home(request):
    return render(request, "Predictor.html")

def ImpLinks(request):
    return render(request, "ImportantLink.html")

def Distribution(request):
    return render(request, "distribution.html")

def helpUS(request):
    return render(request, "help.html")

def aboutUS(request):
    return render(request, "about.html")

# def formInfo(request):
#     if request.method == 'POST':
#         print(request.POST.get('Region'))
#         return render(request, 'Predictor.html')
#     #predicted_power_load[0][0]

#     return render(request, 'Predictor.html')
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def Menu(request):
    return render(request,'Menu.html')
def About(request):
    return render(request,'About.html')
def Contact(request):
    return render(request,'Contact.html')
# def OurService(request):
#     return render(request,'OurService.html')
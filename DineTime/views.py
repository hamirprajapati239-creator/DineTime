from django.shortcuts import render

from DineTime.dine.models import Restaurant

def home(request):
    restaurant = Restaurant.objects.first() 
    context = {
        'restaurant': restaurant,  
    }
    return render(request, 'home.html', context)
def Menu(request):
    return render(request,'Menu.html')
def About(request):
    return render(request,'About.html')
def Contact(request):
    return render(request,'Contact.html')
# def OurService(request):
#     return render(request,'OurService.html')
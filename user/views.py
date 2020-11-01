from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from user.models import Member


def login(request):
    return render(request, 'login.html')

@login_required
def profile(request):
        return render(request, 'profile.html')


def registration(request):
        if request.method=='POST':
                name=request.POST['name']
                email=request.POST['email']
                address=request.POST['address']
                phone=request.POST['phone']
                x = Member(name=name,email=email,address=address, phone=phone)
                x.save()
                return render(request, 'success.html', {'result': name})

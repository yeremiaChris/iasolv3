from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'account/home.html')
def mahasiswa(request):
    return render(request,'account/mahasiswa.html')
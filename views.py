from django.shortcuts import render

def Project1(request):
	return render(request, 'solar/Project1.html')

def Registration(request):
	return render(request, 'solar/Registration.html')

def Login(request):
	return render(request, 'solar/Login.html')

def Dashboard(request):
	return render(request, 'solar/Dashboard.html')

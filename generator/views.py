from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request,'generator/home.html')


def password(request):

	strings = list('abcdefghijklmnopqrstuvwxyz')


	if request.GET.get('uppercase'):
		strings.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	if request.GET.get('Specialcase'):
		strings.extend('!@#$%^&*()')
	if request.GET.get('number'):
		strings.extend('0123456789')

	length = int(request.GET.get('length',12))
	thepassword = ''
	for x in range(length):
		thepassword += random.choice(strings)



	return render(request,'generator/password.html',{'password':thepassword})



def aboutme(request):
	return render(request,'generator/about.html')
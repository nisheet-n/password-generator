from django.shortcuts import render
import random
import string

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def generate(chars,length):
	newpass = ''

	for i in range(-(-length//2)):
		newpass += random.choice(string.ascii_letters)

	for i in range(length - -(-length//2)):
		newpass += random.choice(chars)

	randompass = ''.join(random.sample(newpass,len(newpass)))
	return randompass

def password(request):
	alphabets = string.ascii_lowercase
	length = int(request.GET.get('length', 13))
	passcount = int(request.GET.get('passcount', 1))
	phrase = request.GET.get('include', "")

	if request.GET.get('uppercase'):
		alphabets += string.ascii_uppercase

	if request.GET.get('special'):
		alphabets += string.punctuation

	if request.GET.get('number'):
		alphabets += string.digits
	
	finalpass = [generate(alphabets,length) for i in range(passcount)]	
	
	for i in range(len(finalpass)):		
		if len(phrase) != length:
			start = random.randrange(0, length - len(phrase))		
			finalpass[i] = finalpass[i][:start] + phrase + finalpass[i][start+len(phrase):]		
		else:
			finalpass[i] = phrase
		
	return render(request, 'generator/password.html', {'passwords': finalpass, 'userphrase': phrase})
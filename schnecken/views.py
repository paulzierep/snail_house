from django.shortcuts import render

def home(request):
	print 'home'
	return render(request, 'home.html', {})

def schnecken_bilder(request):
	print 'here'
	return render(request, 'schnecken_bilder.html', {})

def dachwurzen_bilder(request):
	print 'home'
	return render(request, 'dachwurzen_bilder.html', {})

def markt(request):
	print 'here'
	return render(request, 'maerkte.html', {})

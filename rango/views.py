from django.http import HttpResponse

def index(request):
	return HttpResponse('Rango says hello World ! <a href= "/rango/about/"> About </a>')

def about(request):
	return HttpResponse('Rango says : here is the about page <a href="/rango/"> Back </a>')
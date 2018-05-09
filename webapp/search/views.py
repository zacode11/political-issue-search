from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
	if request.method == 'POST':
		search_query = request.POST.get('search')
		print(search_query)
		return HttpResponseRedirect('/results?q=' + search_query)
	return HttpResponse(render(request, 'search/index.html'))

def results(request):
	query = request.GET.get('q', '')
	print(query)
	return HttpResponse(render(request, 'search/results.html'))
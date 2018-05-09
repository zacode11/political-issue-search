from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#import os, sys, inspect

# sys.path.insert(1, os.path.join(sys.path[0], '..'))
# sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import search


def index(request):
	if request.method == 'POST':
		search_query = request.POST.get('search')
		print(search_query)
		return HttpResponseRedirect('/results?q=' + search_query)
	return HttpResponse(render(request, 'app/index.html'))

def results(request):
	query = request.GET.get('q', '')

	#dir_path = os.getcwd()
	print(query)
	#print(dir_path)
	print(search.front_end_search(query, 10))

	return HttpResponse(render(request, 'app/results.html'))
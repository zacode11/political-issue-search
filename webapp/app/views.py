from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import os, sys, inspect

sys.path.insert(1, os.path.join(sys.path[0], '..'))
# sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import search
import json


def index(request):
	if request.method == 'POST':
		search_query = request.POST.get('search')
		print(search_query)
		return HttpResponseRedirect('/results?q=' + search_query)
	return HttpResponse(render(request, 'app/index.html'))

def results(request):
	query = request.GET.get('q', '')

	print(query)
	os.chdir('..')
	os.system('python search.py \"{}\" {} -f'.format(query, str(10)))
	with open('results.json', 'r') as f:
		results = json.load(f)
	print(results)
	os.chdir('webapp')

	context = {
		'query': query,
		'results': results,
	}

	return HttpResponse(render(request, 'app/results.html', context)) 
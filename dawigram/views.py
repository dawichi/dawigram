"""Dawigram views
"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
	# Returns a greeting
	now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
	return HttpResponse(f'Hello World! Current server time is {str(now)}')

def hi(request):
	# import pdb; pdb.set_trace()
	numbers = [int(x) for x in request.GET['numbers'].split(',')]
	sorted_numbers = sorted(numbers)
	data = {
		'status': 'ok',
		'numbers': sorted_numbers,
		'message': 'Integers sorted successfully'
	}
	return HttpResponse(json.dumps(data), content_type='application/json')
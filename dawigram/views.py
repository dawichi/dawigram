"""Dawigram views
"""

# Django
from django.http import HttpResponse
from django.utils import datastructures

# Utilities
from datetime import datetime
import json

def hello_world(request):
	"""Returns a greeting."""
	now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
	return HttpResponse(f'Hello World! Current server time is {str(now)}')

def sort_integers(request):
	"""Returns a JSON with sorted integers loaded by GET."""
	#import pdb; pdb.set_trace()
	numbers = [int(x) for x in request.GET['numbers'].split(',')]
	sorted_numbers = sorted(numbers)
	data = {
		'status': 'ok',
		'numbers': sorted_numbers,
		'message': 'Integers sorted successfully'
	}
	return HttpResponse(
		json.dumps(data),
		content_type='application/json'
	)


def say_name(request, name, age):
	"""Returns a greeting with your name and age."""
	if age < 12:
		message = f'Sorry {name}, you are not allowed here'
	else:
		message = f'Hello {name}! Welcome to Dawigram!'
	return HttpResponse(message)
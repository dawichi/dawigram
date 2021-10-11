"""Posts views."""
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime


posts = [
	{
		'title': 'Mont Blanc',
		'user': {
			'name': 'David Fajardo',
			'picture': 'https://picsum.photos/60/60/?image=1027'
		},
		'timestamp': datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
		'picture': 'https://picsum.photos/800/600?image=1036',
	},
	{
		'title': 'Milky Way',
		'user': {
			'name': 'John Carter',
			'picture': 'https://picsum.photos/60/60/?image=1005'
		},
		'timestamp': datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
		'picture': 'https://picsum.photos/800/600?image=903',
	},
	{
		'title': 'Some building',
		'user': {
			'name': 'Antonio García',
			'picture': 'https://picsum.photos/60/60/?image=883'
		},
		'timestamp': datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
		'picture': 'https://picsum.photos/800/600?image=1076',
	}
]

def list_posts(request):
	"""List existing posts."""
	return render(request, 'feed.html', {'posts': posts})
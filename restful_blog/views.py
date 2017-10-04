from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from datetime import datetime
import json

def index(request):
    return render(request, 'index.html')


def format_timestamp(dt):
	return dt.strftime('%d, %b, %Y')


def get_latest_post(request):
	timestamp = format_timestamp(datetime.utcnow())
	response = JsonResponse(json.dumps({
			'title': 'Test Title!',
			'timestamp': timestamp,
			'description': 'Wow! This is a description, but we\'ve got a lot more to say in the actual post!',
			'thumbnail': 'https://deadlink.com',
			'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
		}), safe=False
	)
	return response

# TODO

def get_all_posts(request, page=0):
	timestamp = format_timestamp(datetime.utcnow())
	response = JsonResponse(json.dumps({
			'total': 2,
			'page': page,
			'posts': {
				{
					'title': 'Test Title!',
					'timestamp': timestamp,
					'description': 'Wow! This is a description, but we\'ve got a lot more to say in the actual post!',
					'thumbnail': 'https://deadlink.com',
					'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
				},
				{
					'title': 'Test, slightly older Title!',
					'timestamp': timestamp,
					'description': 'Wow! This is a description, but we\'ve got a lot more to say in the actual post!',
					'thumbnail': 'https://deadlink.com',
					'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
				},
			}
		}), safe=False
	)
	return response
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def get_latest_entry(request):
	return HttpResponse(200)


def paginated_entries(request):
	return HttpResponse(200)
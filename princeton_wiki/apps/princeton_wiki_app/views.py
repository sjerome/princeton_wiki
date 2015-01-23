from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def index(request):
	context = {}
	return render(request, "index.html", context);
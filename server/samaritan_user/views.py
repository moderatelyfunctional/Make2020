import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from samaritan_user.models import SamaritanState

# Create your views here.
def index(request):
	context = dict()
	# first = SamaritanState.objects.create(driver='default', state='nr')
	# first.save()
	state = SamaritanState.objects.all().first()
	return render(request, 'index.html', context)

@csrf_exempt
def drive(request):
	data = json.loads(request.body)
	key = data['key']
	print(key)
	return HttpResponse(json.dumps({'response': 'Got it'}), status=200)


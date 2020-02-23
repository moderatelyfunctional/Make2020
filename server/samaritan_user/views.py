import json

from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from motor_commands import move_both, forward, stop

# Create your views here.
def index(request):
	context = dict()
	return render(request, 'index.html', context)

@csrf_exempt
def drive(request):
	data = json.loads(request.body)
	key = data['key']
	print(key)
	if key == 'up':
		forward()
	else:
		stop()



	return HttpResponse(json.dumps({'response': 'Got it'}), status=200)

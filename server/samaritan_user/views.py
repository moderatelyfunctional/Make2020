import json

from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

from samaritan_user.models import SamaritanState, SamaritanKeyDown
from samaritan_user.camera import CustomPiCam

cam = None

# Create your views here.
def index(request):
	if cam = None:
		cam = CustomPiCam()

	context = dict()
	state = SamaritanState.objects.all().first()
	return render(request, 'index.html', context)

@csrf_exempt
def drive(request):
	data = json.loads(request.body)
	key_down = SamaritanKeyDown.objects.all().first()

	return HttpResponse(json.dumps({'response': 'Got it'}), status=200)

def gen(camera):
	while True:
		frame = cam.get_frame()
		yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def feed(request):
	try:
		return StreamingHttpResponse(gen(PiCam()), content_type='multipart/x-mixed-replace;boundary=frame')
	except:
		pass
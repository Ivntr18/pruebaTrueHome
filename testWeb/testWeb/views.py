from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
	return render(request, 'main.html')


def dameFecha(request):
	fecha_actual=datetime.datetime.now()
	documento= """ <html>
	<body>
	<h1>
	Fecha y hora actuales %s
	</h1>
	</body>
	</html>""" % fecha_actual

	return HttpResponse(documento)

def calculaEdad(request, agno,edad):
	edadActual=edad
	periodo=agno-2019
	edadFutura=edadActual+periodo
	documento= """ <html>
	<body>
	<h1>
	En el año %s tendrás %s años
	</h1>
	</body>
	</html>""" % (agno,edadFutura)

	return HttpResponse(documento)

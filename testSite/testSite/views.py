from django.http import HttpResponse
import datetime

def saludo(request):
	return HttpResponse("HOla")


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

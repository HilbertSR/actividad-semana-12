import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Libro

@method_decorator(csrf_exempt, name="dispatch")
class ProyectoView(View):

    def get(self, request):
        getLibro = list(Libro.objects.values("id", "nombre", "autor"))
        return JsonResponse(getLibro, safe=False)

    def post(self, request):
        datos = json.loads(request.body)
        postLibro = Libro.objects.create(
            nombre=datos["nombre"],
            autor=datos.get("autor", ""),
        )
        return JsonResponse({"id": postLibro.id}, status=201)

    def put(self, request, pk):
        datos = json.loads(request.body)
        putLirbo = Libro.objects.get(pk=pk)
        putLirbo.nombre = datos.get("nombre", putLirbo.nombre)
        putLirbo.autor = datos.get("autor", putLirbo.autor)
        putLirbo.save()
        return JsonResponse({"mensaje": "Libro actualizado"})

    def delete(self, request, pk):
        Libro.objects.get(pk=pk).delete()
        return JsonResponse({"mensaje": "Libro eliminado"})
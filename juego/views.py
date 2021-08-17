from django.shortcuts import redirect, render
from .models import Partida, Respuesta, Pregunta, Categoria
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def listar_preguntas(request):
    """ #respuestas = Pregunta.objects.order_by("?") # Una forma de hacer un random en la consulta
    respuestas = Pregunta.objects.all() # traigo todos los registros de la consulta
    return render(request, "juego/listar_preguntas.html",{"nombre":"Leonardo", "respuesta": respuestas}) """
    
    if request.method == "POST":

        resultado = 0
        for i in range(1,3):
            opcion = Respuesta.objects.get(pk=request.POST[str(i)])
            resultado += opcion.puntaje
        Partida.objects.create(usuario=request.user,fecha=datetime.now,resultado=resultado)
        return redirect("/")
        #pass
    else:
        data={}
        preguntas = Pregunta.objects.all().order_by('?')[:2]
        for item in preguntas:
            respuestas = Respuesta.objects.filter(id_pregunta=item.id)
            categoria = Categoria.objects.get(pk=item.id_categoria.id)
            data[item.pregunta]= {"opciones": respuestas, "categoria":categoria}
        return render(request,"juego/listar_preguntas.html",{"preguntas": preguntas ,"data": data}) 

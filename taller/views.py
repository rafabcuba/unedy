from django.db.models import F, Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.db.models.functions import ExtractMonth
from calendar import month_name
import locale
from django.contrib.auth.decorators import login_required

from .models import Choice, Question, Registro, Prioridad, Entidad, Especialista
from .forms import CreateRegistroForm, CreatePrioridadForm

# Create your views here.

# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]

@login_required(login_url="/login/")
def index(request):
    title = f'Estado general del taller'
    
    total_registro_list = (Registro.objects
          .values('entidad__nombre')  # Group by entidad
          .annotate(ecount=Count('entidad'))  # Count registers for each entidad
          .order_by('-ecount')  # Optional: Ensure correct sorting
          )[:15]
    entidad_nombres = total_registro_list.values_list('entidad__nombre', flat=True)
    entidad_nombres = list(entidad_nombres)
    ecount_values = total_registro_list.values_list('ecount', flat=True)
    ecount_values = list(ecount_values)
    
    registros_x_estado_list = (Registro.objects
          .values('estado')
          .annotate(estcount=Count('estado'))
          )
    
    estado_nombres = registros_x_estado_list.values_list('estado', flat=True)
    estado_nombres = list(estado_nombres)
    estcount_values = registros_x_estado_list.values_list('estcount', flat=True)
    estcount_values = list(estcount_values)
    
    solucionados = Registro.objects.filter(solucionado=True).count()
    no_solucionados = Registro.objects.filter(solucionado=False).count()
    total_registros = Registro.objects.count()
    
    registros_por_mes = (Registro.objects
                     .annotate(mes=ExtractMonth('fecha_entrada'))
                     .values('mes')
                     .annotate(total_registros=Count('id'))
                     .order_by('mes'))
    locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
    meses_en_espanol = {i: month_name[i] for i in range(1, 13)}
    resultados_registros_por_mes = [{'mes': meses_en_espanol[registro['mes']], 'total_registros': registro['total_registros']}
                                    for registro in registros_por_mes]
    
    # total_registros_x_mes = resultados_registros_por_mes.values_list('total_registros', flat=True)
    # total_registros_x_mes = list(total_registros_x_mes)
    # meses = resultados_registros_por_mes.values_list('mes', flat=True)
    # meses = list(meses)
    
    meses = [entry['mes'] for entry in resultados_registros_por_mes]
    total_registros_x_mes = [entry['total_registros'] for entry in resultados_registros_por_mes]
    
    
    context = {
        'title': title,
        'entidades': entidad_nombres,
        'totalregistros': ecount_values,
        'estados': estado_nombres,
        'estcount': estcount_values,
        'solucionados': solucionados,
        'no_solucionados': no_solucionados,
        'total_registros': total_registros,
        'total_registros_x_mes': total_registros_x_mes,
        'meses': meses,
        }
    return render(request, 'taller/index.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("taller:results", args=(question.id,)))


class RegistroIndexView(generic.ListView):
    model = Registro
    template_name = "taller/registro.html"
    
    # def get_queryset(self):
    #     queryset = Registro.objects.all()
    #     return queryset.order_by('fecha_entrada')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de recepciones'
        return context


class PrioridadListView(generic.ListView):
    model = Prioridad
    template_name = "taller/prioridades_list.html"

@login_required(login_url="/login/")
def create_prioridad_view(request):
    if request.method == 'POST':
        form = CreatePrioridadForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('taller:prioridades-list'))
    else:
        form = CreatePrioridadForm()
    context = {'form': form}
    return render(request, 'taller/create_prioridad.html', context)

@login_required(login_url="/login/")
def create_registro_view(request):
    if request.method == 'POST':
        form = CreateRegistroForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('taller:registro'))
    else:
        form = CreateRegistroForm()
    context = {'form': form}
    return render(request, 'taller/create_registro.html', context)

@login_required(login_url="/login/")
def date_selector(request, reporte=None):
    if request.method == 'POST':
        fecha_inicial=request.POST['fecha_inicial']
        fecha_final=request.POST['fecha_final']
        if reporte == 'registro':
            title = f'Registro de recepciones desde {fecha_inicial}, hasta {fecha_inicial}'
            registro_list = Registro.objects.filter(fecha_entrada__range=(fecha_inicial, fecha_final))
            context = {
                'title': title,
                'registro_list': registro_list,
                }
            return render(request, 'taller/registro.html', context)
        
        if reporte == 'indicadores':
            title = f'indicadores {fecha_inicial}, hasta {fecha_inicial}'
            pass
        
    context = {}
    return render(request, 'wizards/date_selector.html', context)

@login_required(login_url="/login/")
def entidad_selector(request, reporte=None):
    if request.method == 'POST':
        entidad_id=request.POST['entidad_id']
        if reporte == 'registro':
            entidad_seleccionada = Entidad.objects.get(id=entidad_id)
            title = f'Registro de recepciones por entidad ({entidad_seleccionada.nombre})'
            registro_list = Registro.objects.filter(entidad=entidad_id)
            context = {
                'title': title,
                'registro_list': registro_list,
                }
            return render(request, 'taller/registro.html', context)
    
    entidad_list = Entidad.objects.all()
    context = {'entidad_list': entidad_list,}
    return render(request, 'wizards/entidad_selector.html', context)

@login_required(login_url="/login/")
def prioridad_selector(request, reporte=None):
    if request.method == 'POST':
        prioridad_id=request.POST['prioridad_id']
        if reporte == 'registro':
            prioridad_seleccionada = Prioridad.objects.get(id=prioridad_id)
            title = f'Registro de recepciones por prioridad ({prioridad_seleccionada.nombre})'
            registro_list = Registro.objects.filter(prioridad=prioridad_id)
            context = {
                'title': title,
                'registro_list': registro_list,
                }
            return render(request, 'taller/registro.html', context)
    
    prioridad_list = Prioridad.objects.all()
    context = {'prioridad_list': prioridad_list,}
    return render(request, 'wizards/prioridad_selector.html', context)

@login_required(login_url="/login/")
def especialista_selector(request, reporte=None):
    if request.method == 'POST':
        especialista_id=request.POST['especialista_id']
        if reporte == 'registro':
            especialista_seleccionado = Especialista.objects.get(id=especialista_id)
            title = f'Registro de recepciones por especialista ({especialista_seleccionado.nombre})'
            registro_list = Registro.objects.filter(especialista=especialista_id)
            context = {
                'title': title,
                'registro_list': registro_list,
                }
            return render(request, 'taller/registro.html', context)
    
    especialista_list = Especialista.objects.all()
    context = {'especialista_list': especialista_list,}
    return render(request, 'wizards/especialista_selector.html', context)

@login_required(login_url="/login/")
def estado_selector(request, reporte=None):
    if request.method == 'POST':
        estado_id=request.POST['estado_id']
        if reporte == 'registro':
            estado_seleccionado = estado_id
            title = f'Registro de recepciones por estado ({estado_seleccionado})'
            registro_list = Registro.objects.filter(estado=estado_id)
            context = {
                'title': title,
                'registro_list': registro_list,
                }
            return render(request, 'taller/registro.html', context)
    
    estado_list = [
        {"id": "RECEPCIONADO", "nombre": "Recepcionado"},
        {"id": "ASIGNADO", "nombre": "Asignado"},
        {"id": "EVALUADO", "nombre": "Evaluado"},
        {"id": "EN_PROCESO", "nombre": "En proceso"},
        {"id": "FINALIZADO", "nombre": "Finalizado"},
    ]
    context = {'estado_list': estado_list,}
    return render(request, 'wizards/estado_selector.html', context)

@login_required(login_url="/login/")
def grafica_detalle_x_entidad(request):
    title = f'Registro por entidades'
    
    detalle_registro_list = (Registro.objects
          .values('entidad__nombre')  # Group by entidad
          .annotate(ecount=Count('entidad'))  # Count registers for each entidad
          .order_by('-ecount')  # Optional: Ensure correct sorting
          )[:10]
    
    context = {
        'title': title,
        'detalle_registro_list': detalle_registro_list,
        }
    
    return render(request, 'graficas/detalle_x_entidad.html', context)

@login_required(login_url="/login/")
def grafica_total_x_entidad(request):
    title = f'Registro por entidades'
    
    total_registro_list = (Registro.objects
          .values('entidad__nombre')  # Group by entidad
          .annotate(ecount=Count('entidad'))  # Count registers for each entidad
          .order_by('-ecount')  # Optional: Ensure correct sorting
          )[:15]
    
    # entidades = total_registro_list(entidad)
    
    entidad_nombres = total_registro_list.values_list('entidad__nombre', flat=True)
    entidad_nombres = list(entidad_nombres)
    
    ecount_values = total_registro_list.values_list('ecount', flat=True)
    ecount_values = list(ecount_values)
    
    context = {
        'title': title,
        'total_registro_list': total_registro_list,
        'entidades': entidad_nombres,
        'totalregistros': ecount_values,
        }
    
    return render(request, 'graficas/total_x_entidad.html', context)

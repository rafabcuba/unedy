from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Choice, Question, Registro, Prioridad
from .forms import CreateRegistroForm, CreatePrioridadForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

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
    
    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileDetailView, self).get_context_data(**kwargs) # get the default context data
    #     context['voted_links'] = Link.objects.filter(votes__voter=self.request.user) # add extra field to the context
    #     return context


# def prioridad_list_view(request):
#     prioridades = Prioridad.objects.all()
#     context = {'prioridades': prioridades}
#     return render(request, 'taller/prioridades_list.html', context)

class PrioridadListView(generic.ListView):
    model = Prioridad
    template_name = "taller/prioridades_list.html"

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
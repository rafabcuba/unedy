from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Registro

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template("polls/index.html")
#     context = {"latest_question_list": latest_question_list,}
#     # return HttpResponse(template.render(context, request))
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

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


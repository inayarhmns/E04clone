from django.shortcuts import render
from django.http import response, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Faq
from .forms import FormFaq
import json

# Create your views here.
def index(request):
    form = FormFaq()
    faqs = Faq.objects.all()
    response = {
        'title':'F.A.Q - Irama Kain',
        'faqs': faqs,
        'form': form
    }
    if request.user.is_authenticated:
        return render(request, 'faq_loggedin.html', response)
    else:
        return render(request, 'faq.html', response)

def create_question(request):
    data = dict()
    if request.method == "POST":
        form = FormFaq(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            question = request.POST['question']
            faq = Faq(question = question)
            faq.save()
            question = Faq.objects.values()
            data['question'] = list(question)
            return JsonResponse(data)
        else: 
            data['form_is_valid'] = False
            return JsonResponse(data)

@csrf_exempt
def answer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        question_answer = Faq(question = data['question'], answer = "")
        question_answer.save()
    faqs = Faq.objects.all()
    faq_data = json.loads(serializers.serialize('json', faqs))
    return JsonResponse(faq_data, safe = False)

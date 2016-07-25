from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from voices.models import *
from voices.forms import * 
from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView
import logging
import json
import sys
from datetime import datetime
logr = logging.getLogger(__name__)

'''
TEMPLATES = { "voices" : "voices/items.html",
              "cart" : "voices/cart.html"
            }
'''

def index(request):
    template = loader.get_template('voices/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def items(request):
    
    if request.method == 'POST':
        
        produce = Products.objects.filter(prodType="produce")
        canned = Products.objects.filter(prodType="canned")
        boxed = Products.objects.filter(prodType="boxed")
        grains = Products.objects.filter(prodType="grainsBeans")
        household = Products.objects.filter(prodType="household")
        clothing = Products.objects.filter(prodType="clothing")
        satisfactionData = request.POST.get('faceChosen')
        template = loader.get_template('voices/items.html')
        context = {'satisfactionData': satisfactionData,
                   'produce': produce,
                   'canned': canned,
                   'boxed': boxed,
                   'grains': grains,
                   'household': household,
                   'clothing': clothing
               }

        return HttpResponse(template.render(context, request))

    else:
        produce = Products.objects.filter(prodType="produce")
        canned = Products.objects.filter(prodType="canned")
        boxed = Products.objects.filter(prodType="boxed")
        grains = Products.objects.filter(prodType="grainsBeans")
        household = Products.objects.filter(prodType="household")
        clothing = Products.objects.filter(prodType="clothing")

        template = loader.get_template('voices/items.html')
        context = {'produce': produce,
                   'canned': canned,
                   'boxed': boxed,
                   'grains': grains,
                   'household': household,
                   'clothing': clothing}

        return HttpResponse(template.render(context, request))


def cart(request):
    if request.method == 'POST':
        chosen = request.POST.getlist('ab[]')
        why = request.POST.getlist('why[]')
        satisfactionData = request.POST.get('faceChosen')
        suggestedItems = request.POST.get('suggestions')
       
        chosenObj = []

        for i in range(len(chosen)):
            chosenObj.append(Products.objects.get(pk=chosen[i]))

        template = loader.get_template('voices/cart.html')
        context = {'prodChosen': chosenObj,
                   'why': why,
                   'suggestions': suggestedItems,
                   'satisfactionData': satisfactionData,
                   }

        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('voices/cart.html')
        context = {}
        return HttpResponse(template.render(context, request))

def thanks(request):
    if request.method == 'POST':
        chosen = request.POST.getlist('selected[]')
        why = request.POST.getlist('whyReason[]')
        suggestedItems = request.POST.get('suggestions')
        satisfactionData = request.POST.get('faceChosen')

        zipcode = request.POST.get('zipcode')
        bday = request.POST.get('bday')
        gender = request.POST.get('gender')
        ethnicitySel = request.POST.get('ethnicitySel')
        diet = request.POST.get('dietRest')
        religiousDiet = request.POST.get('religiousDiet')

        reqFin = Request()
        for i in range(len(chosen)):
            if i == 0:
                reqFin.request1 = Products.objects.get(pk=chosen[i]).prodName
            elif i == 1:
                reqFin.request2 = Products.objects.get(pk=chosen[i]).prodName
            elif i == 2:
                reqFin.request3 = Products.objects.get(pk=chosen[i]).prodName

        for i in range(len(why)):
            if i == 0:
                reqFin.why1 = why[i]
            elif i == 1:
                reqFin.why2 = why[i]
            elif i == 2:
                reqFin.why3 = why[i]



        reqFin.additionalItems=suggestedItems
        reqFin.satisfaction=satisfactionData
        reqFin.ethnicitySel=ethnicitySel
        reqFin.zipcode=zipcode
        reqFin.birthday=bday
        reqFin.gender=gender
        reqFin.diet = diet
        reqFin.religiousDiet = religiousDiet
        reqFin.save()

        print(reqFin.zipcode, file=sys.stderr)
        print(reqFin.additionalItems, file=sys.stderr)
        print(reqFin.satisfaction, file=sys.stderr)
        print(reqFin.ethnicitySel, file=sys.stderr)
        print(reqFin.birthday, file=sys.stderr)
        print(reqFin.gender, file=sys.stderr)
        print(reqFin.diet, file=sys.stderr)
        print(reqFin.religiousDiet, file=sys.stderr)

        template = loader.get_template('voices/thanks.html')
        context = {'thanks': 'Thank you for your time'
                   }

        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('voices/thanks.html')
        context = {}
        return HttpResponse(template.render(context, request))


def satisfaction(request):
    template = loader.get_template('voices/satisfaction.html')
    context = {}
    return HttpResponse(template.render(context, request))
    



'''
def process_form_data(form_list):
    # add to db
    form_data = [form.cleaned_data for form in form_list]

    # adds into db
    elem = Request(request1 = form_data[0]['request1'], 
                   request2 = form_data[0]['request2'], 
                   request3 = form_data[0]['request3'], 
                   why = form_data[1]['why'], )
    elem.save()

    return form_data

class ContactWizard(SessionWizardView):
    # template_name = "voices/voices_form.html"

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]
    

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return render_to_response('voices/done.html', {'form_data':form_data}) 
        # prints out data in the form

'''

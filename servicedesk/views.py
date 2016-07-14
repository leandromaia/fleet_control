from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from django.http import HttpResponseRedirect

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Processa os dados no form.cleaned_data
            # ...
            return HttpResponseRedirect('/servicedesk/thanks')
    else:
        form = ContactForm()

    return render_to_response('contact.html', {'form': form,},  \
                                            RequestContext(request))

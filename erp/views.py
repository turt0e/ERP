from django.shortcuts import render
from .forms import ContactForm

def contact_page(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)

    else:
        contact_form = ContactForm()

    context = {
        'form': contact_form
    }
    return render(request, 'contact/contact.html', context)



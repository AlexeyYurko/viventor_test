# from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views import generic

from .forms import CreateContactForm
from .models import Contact


class ContactsList(generic.ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contact_list.html'


def new_contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = CreateContactForm()
    return render(request, 'add_contact.html', {'form': form})

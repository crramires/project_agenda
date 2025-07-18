from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contact.forms import ContactForm
from django.urls import reverse

from contact.models import Contact

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST': 
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action
        }
        
        if form.is_valid():
            contact = form.save()
            return redirect(
                'contact:update',
                contact_id=contact.id
            )

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(),
        'form_action': form_action
    }
    
    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact,
        id=contact_id,
        show=True,
        owner=request.user
    )

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id=contact.id)
        
        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, id=contact_id, show=True, owner=request.user
    )
    
    confirm_delete = request.POST.get('confirm_delete', 'no')
    if confirm_delete == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirm_delete': confirm_delete,
        }

    )


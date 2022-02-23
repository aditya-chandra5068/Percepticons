from django.shortcuts import render
from django.contrib import messages
from contact.models import Contact

def contact(request):
    """
    function to save the data to the Contact Model (Contact database table) when data entered from UI side
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('content')
        contact = Contact(name=name, email=email, subject=subject, content=msg)
        contact.save()
        messages.success(request, "Your response has been saved.")
    context = {
            'current_page':'contact'           
        }            
    return render(request, 'contact/contact.html', context)

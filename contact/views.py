from django.shortcuts import render
from django.contrib import messages
from contact.models import Contact

def contact(request):
    """
    function to save the data to the Contact Model (Contact database table) when data entered from UI side
    """
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['content']
        contact = Contact(name=name, email=email, subject=subject, content=msg)
        contact.save()
        messages.success(request, "Your response has been saved.")
    context = {
            'current_page':'contact'           
        }            
    return render(request, 'contact/contact.html', context)

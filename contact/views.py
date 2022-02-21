from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib import messages
from contact.models import Contact

from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate, logout 
from django.conf import settings
from django.core.mail import send_mail




def contact(request):
    if request.method == 'POST':
        # print("we are using post request")
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['content']

        print(name," --- ", email, " --- ", subject, " --- ", msg)
        # if len(name)<2: 
        #     messages.error(request, "Please fill the name correctly")

        # elif len(email)<3:
        #     messages.error(request, "Plese fill the email correctly")

        # elif len(phone)<10 or len(phone)>14:
        #     messages.error(request, "Plese fill the phone number correctly")
        
        # elif len(msg)<4:
        #     messages.error(request, "Plese describe your issue correctly")
        # else:            
        #     contact = Contact(name=name, email = email, phone = phone, content = msg)
        #     contact.save()
        #     messages.success(request, "Your response has been saved.")
        contact = Contact(name=name, email=email, subject=subject, content=msg)
        contact.save()
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [settings.EMAIL_HOST_USER]
        # send_mail(subject, f"You have new mail from {name}, email: {email}", email_from, recipient_list)

        messages.success(request, "Your response has been saved.")



    context = {
            'current_page':'contact'           
        }            
    return render(request, 'contact/contact.html', context)

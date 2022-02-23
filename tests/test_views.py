from django.test import TestCase, Client
from django.urls import reverse
from contact.models import Contact
from contact.views import contact

class TestViews(TestCase):
    """
    to test view of contact app
    """
    def setUp(self):
        self.client = Client()
        self.contact_url = reverse(contact)

    def contact_post(self):
        response = self.client.post(self.contact_url,{
            'sno' : 1,
            'name' : 'Python Language',
            'subject' : 'Python Tutorial',
            'email' : 'pythontutorial123@gmail.com',
            'content' : 'This is just a demo content',
            'timeStamp' : 'Feb 23, 2022, 5:11 a.m.'
        })
        self.assertTemplateUsed(response,'contact/contact.html')
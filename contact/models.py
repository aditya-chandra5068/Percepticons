from django.db import models

class Contact(models.Model):
    """
    Class Model being used to create a Contact table in database (Contact database table creation)
    """
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f""" Message from {self.name}, Email: {self.email} """
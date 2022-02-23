from django.db import models

class Topic(models.Model):
    """
    Class model to create table for topic in database (Topic database table creation)
    """
    topic_id = models.AutoField(primary_key=True)
    topic_name = models.CharField(max_length=100)
    topic_image = models.CharField(max_length=200)

    def __str__(self):
        return f"""{self.topic_name}"""        

class Post(models.Model):
    """
    Class model to create table for Post being saved from admin pannel to database (Post database table creation)
    """
    PUBLISH = True
    DRAFT = False

    STATUS_CHOICES = [(PUBLISH, 'publish'), (DRAFT, 'draft')]

    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keywords = models.CharField(max_length=255)
    background_image = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    is_publish = models.BooleanField(
                                max_length=10,
                                choices=STATUS_CHOICES,
                                default=DRAFT,)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateField(blank=True)

    def __str__(self):
        return f""" {self.title} by {self.author} {self.slug}"""

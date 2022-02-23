import imp
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from home.views import home,topic,search
from contact.views import contact
from about.views import about
from blog.views import blogHome,blogPost,editPost

class TestUrls(SimpleTestCase):
    """
    to test urls of every app being registered
    """
    def test_home_home_url_resolved(self):
        url = reverse('home')        
        self.assertEquals(resolve(url).func,home)

    # def test_topic_url_resolved(self):
    #     url = reverse('topic',args=['topic/01'])
    #     self.assertEquals(resolve(url).func,topic)

    def test_home_search_url_resolved(self):
        url = reverse('search')        
        self.assertEquals(resolve(url).func,search)

    def test_contact_contact_url_resolved(self):
        url = reverse('contact')        
        self.assertEquals(resolve(url).func,contact)

    def test_blog_blogHome_url_resolved(self):
        url = reverse('blogHome')        
        self.assertEquals(resolve(url).func,blogHome)

    def test_blog_blogPost_url_resolved(self):
        url = reverse('blogPost',args=['some-slug'])        
        self.assertEquals(resolve(url).func,blogPost)

    def test_blog_editPost_url_resolved(self):
        url = reverse('editPost',args=['some-slug'])        
        self.assertEquals(resolve(url).func,editPost)

    def test_about_about_url_resolved(self):
        url = reverse('about')        
        self.assertEquals(resolve(url).func,about)


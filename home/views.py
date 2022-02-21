from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Topic, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def home(request):
    allTopics = Topic.objects.all()
    # allPosts = Post.objects.all().order_by('-timeStamp')[:4]
    allPosts = Post.objects.filter(is_publish=True)

    context = {
        'allPosts':allPosts,
        'allTopics':allTopics,
        'current_page':'home'
    }
    return render(request, 'home/home.html', context)


def topic(request, topic_id):

    topic_name = Topic.objects.get(topic_id=topic_id)
    print("TOPIC name: ",topic_name)
    topic_id_posts = Post.objects.filter(topic_id=topic_id)
    # allPostsTitle = Post.objects.filter(title__icontains=topic_name)
    # allPostsContent = Post.objects.filter(content__icontains=topic_name)
    # allPosts = allPostsTitle.union(allPostsContent)

    paginator = Paginator(topic_id_posts    , 5)
    page_number = request.GET.get("page")

    current_topic = topic_name
    try:
        # posts = paginator.page(page_number)
        posts = paginator.get_page(page_number)
        # posts.paginator.page_range
        # print("---------- has next: ", posts.has_next)

    except PageNotAnInteger as e:
        posts = paginator.page(1)
        posts = paginator.get_page(1)

    except EmptyPage:
        # posts = paginator.page(paginator.num_pages)
        posts = paginator.get_page(paginator.num_pages)

    allTopics = Topic.objects.all()
    print(posts)
    print("PAGINATOR",[f"{i}" for i in posts])


    # if allPosts.count() == 0:
    #     messages.warning(request, "Please search correctly.")        

    allTopics = Topic.objects.all()
    params = {'allPosts': posts,
            'allTopics':allTopics,
            'topic_name':topic_name,
            'current_page':'topic',
            'current_topic': current_topic
            }   

    return render(request, 'home/topic.html', params)   
           



def search(request):
    query = request.GET['query']
    if len(query)>70:
        # allPosts=[]
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        

    # if allPosts.count() == 0:
    #     messages.warning(request, "Please search with correct")        
    current_page = 'search_page'
    allTopics = Topic.objects.all()
    params = {'allPosts': allPosts,
                'allTopics':allTopics,
                'query':query,
                'current_page':'search_page'}
    return render(request, 'home/search.html', params)           
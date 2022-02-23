from django.shortcuts import render
from blog.models import Topic, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    """
    function to get the data from Model (database table) and render it to front end
    """
    allTopics = Topic.objects.all()
    allPosts = Post.objects.filter(is_publish=True)
    context = {
        'allPosts':allPosts,
        'allTopics':allTopics,
        'current_page':'home'
    }
    return render(request, 'home/home.html', context)

def topic(request, topic_id):
    """
    function to get topic data from Model (database table) and render it to front end with pagination
    """
    topic_name = Topic.objects.get(topic_id=topic_id)
    topic_id_posts = Post.objects.filter(topic_id=topic_id)
    paginator = Paginator(topic_id_posts    , 5)
    page_number = request.GET.get("page")
    current_topic = topic_name
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    allTopics = Topic.objects.all()
    allTopics = Topic.objects.all()
    params = {'allPosts': posts,
            'allTopics':allTopics,
            'topic_name':topic_name,
            'current_page':'topic',
            'current_topic': current_topic
            }   
    return render(request, 'home/topic.html', params)   
           
def search(request):
    """
    function to search the query data from Post's Model (Post database table) and render the result obtained
    """
    query = request.GET['query']
    if len(query)>70:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)        
    current_page = 'search_page'
    allTopics = Topic.objects.all()
    params = {'allPosts': allPosts,
                'allTopics':allTopics,
                'query':query,
                'current_page':'search_page'}
    return render(request, 'home/search.html', params)           
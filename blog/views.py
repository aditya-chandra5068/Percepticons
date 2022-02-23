from django.shortcuts import render
from blog.models import Post, Topic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blogHome(request):
    """
    function to get the blogHome data (like current_page,etc) from Post Model (Post database table) and render it to front end
    """
    allPosts = Post.objects.filter(is_publish=True)
    allPosts = allPosts[::-1]
    paginator = Paginator(allPosts, 5)
    page_number = request.GET.get("page")
    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    allTopics = Topic.objects.all()
    context = {'allPosts':posts,
                'allTopics':allTopics,
                'current_page':'blogHome'}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    """
    function to get the blogPost data (like span topic,etc) from Post Model (Post database table) and render it to front end,
    """
    try:
        post = Post.objects.filter(slug=slug).first()
        span_topic = Topic.objects.filter(topic_id=post.topic_id)
        allTopics = Topic.objects.all()
        context = {'post':post,
                    'allTopics':allTopics,
                    'current_page':'blogPost',
                    'span_topic':span_topic[0]}
        return render(request, 'blog/blogPost.html', context)
    except Exception as e:
        print(e)

def editPost(request, slug):
    """
    function to get the data from Post Model (Post database table) after it has been edited and then render it to front end,
    this functionality is incomplete as from UI side the function to send edited data through AJAX call is still pending.
    """
    try:
        post = Post.objects.filter(slug=slug).first()
        span_topic = Topic.objects.filter(topic_id=post.topic_id)
        allTopics = Topic.objects.all()
        context = {'post':post,
                    'allTopics':allTopics,
                    'current_page':'editPost',
                    'span_topic':span_topic[0]} 
        return render(request, 'blog/edit.html',context)
    except Exception as e:
        print(e)



     
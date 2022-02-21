from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post, Topic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def blogHome(request):
    allPosts = Post.objects.filter(is_publish=True)
    # allPosts = reversed(allPosts)
    allPosts = allPosts[::-1]
    print(allPosts)
    paginator = Paginator(allPosts, 5)
    page_number = request.GET.get("page")

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

    context = {'allPosts':posts,
                'allTopics':allTopics,
                'current_page':'blogHome'}
    return render(request, 'blog/blogHome.html', context)
    


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    span_topic = Topic.objects.filter(topic_id=post.topic_id)
    allTopics = Topic.objects.all()
    context = {'post':post,
                'allTopics':allTopics,
                'current_page':'blogPost',
                'span_topic':span_topic[0]}
    # context= {'post':post} 
    return render(request, 'blog/blogPost.html', context)



     
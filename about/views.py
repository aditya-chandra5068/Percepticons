from django.shortcuts import render

def about(request):
    """
     function to render about details to the UI when "about" endpoint is being hit
    """
    context = {
        'current_page':'about'
    }
    return render(request ,'about/about.html', context) 
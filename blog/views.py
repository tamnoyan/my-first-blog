from django.shortcuts import render

#post_list takes request and return a function render that will render (put together) our template blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html', {})

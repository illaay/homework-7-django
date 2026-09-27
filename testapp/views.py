from django.http import HttpResponse

def hello_user(request, username):
    return HttpResponse(f'<h1>Hello, {username}</h1>!')

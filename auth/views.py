from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.middleware.csrf import get_token
from django.http import HttpResponse

def login_view(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            return render_to_response("auth/login.html", {"error": "username/password incorrect"}, RequestContext(request))
        if "next" in request.GET:
            return redirect(request.GET["next"])
        else:
            return redirect("/")  #go to index if no redirect

    else:
        ctx = RequestContext( request, {
            'csrf_token': get_token( request )
        } )
        return render_to_response("auth/login.html", ctx)

def logout_view(request):
    logout(request)
    return HttpResponse("Logged out successfully.")
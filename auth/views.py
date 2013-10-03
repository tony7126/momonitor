from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.POST:
        user = authenticate(username = "tony", password = "p")
        if user is not None:
            login(request, user)
        else:
            return HttpResponse("bad password")
        if "next" in request.GET:
            return redirect(request.GET["next"])
        else:
            return redirect("/")  #go to index if no redirect

    else:
        return render_to_response("auth/login.html")
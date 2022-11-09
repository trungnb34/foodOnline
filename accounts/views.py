from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django.shortcuts import redirect

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            pass
        return redirect('/')
        # print(form.is_valid())
        # print(form.errors.get_json_data()["__all__"])
    else:
        form = UserForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/registerUser.html", context)

def registerRest(request):
    pass
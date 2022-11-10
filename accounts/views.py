from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django.shortcuts import redirect
from .models import User
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # print(form.errors.as_json())
        if form.is_valid():
            password = form.cleaned_data["password"]
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Your account has been registered sucessfully")
            return redirect('register_user')
    else:
        form = UserForm()
    # print(type(form.errors.values()), form.errors.values())
    context = {
        "form" : form,
        "errors" : form.errors.values()
    }
    return render(request, "accounts/registerUser.html", context)

def registerRest(request):
    pass
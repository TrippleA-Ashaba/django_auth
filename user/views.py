from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    form = UserRegistrationForm()
    return render(request, "user/home.html", {"form": form})


@login_required
def about(request):
    return render(request, "user/about.html")

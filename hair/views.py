from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from hair.forms import InspireUserCreationForm, CommentForm
from hair.models import Comment


def register(request):
    if request.method == 'POST':
        form = InspireUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InspireUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request, 'home.html', )

def about(request):
    return render(request, 'about.html', )

def faq(request):
    return render(request, 'faq.html', )

def medicine(request):
    return render(request, 'medicine.html', )

def law(request):
    return render(request, 'law.html', )

def acting(request):
    return render(request, 'acting.html', )

def sports(request):
    return render(request, 'sports.html', )

def music(request):
    return render(request, 'music.html', )

def programming(request):
    return render(request, 'programming.html', )

def ben_carson(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm()

    return render(request, 'medicine/ben_carson.html', {'form': form})


def vivien_thomas(request):
    return render(request, 'medicine/vivien_thomas.html', )
# def captcha(request):
#     if request.POST:
#         form = InspireUserCreationForm(request.POST)
#
#         # Validate the form: the captcha field will automatically
#         # check the input
#         if form.is_valid():
#             human = True
#     else:
#         form = InspireUserCreationForm()
#
#     return render(request, 'register.html',locals())

def edit(request):
    return render(request, 'edit.html', )
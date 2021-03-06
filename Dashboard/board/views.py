from django.shortcuts import render, redirect 
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile, Trucker
from .forms import ProfileForm, TruckerForm 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/register/')
def board(request):
    truckers = Trucker.objects.all()
    return render(request, 'index.html')

def dashboard(request):
    current_user = request.user
    if request.method == 'POST':
        form = TruckerForm(request.POST, request.FILES)
        if form.is_valid():
            trucker = form.save(commit=False)
            trucker.user=current_user
            trucker.save()
        return redirect('board')

    else:
        form = TruckerForm()
    return render(request, 'dashboard.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['profile_photo']
            profile.user=current_user
            
            profile.save()
        return redirect('board')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def view_profile(request, id):

    profile=Profile.objects.get(user_id=id)
    return render(request, 'view_profile.html',{"profile":profile},)

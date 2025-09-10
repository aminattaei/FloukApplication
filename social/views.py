from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Profile


def home_page(request):
    """
    This view renders the home page.
    """
    # Render the template "Index/index.html" and return it as a response
    return render(request, "Index/index.html", {})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user = request.user)
        return render(request,"social/profile_list.html",{'profiles':profiles})
    else:
        messages.error("You Must Be Logged In View This Page...")
        return redirect("home_page")
    

def profile_detail(request,pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id= pk)
        print(profile.avatar.url)
        print("-" *100)
        print(" media/profile/user_avatar/cropped-2e116631-ca61-408d-b132-1af757a863a7_oWlNC79.png")
        return render(request,"social/profile_detail.html",{'profile':profile})
    
    else:
        messages.error("You Must Be Logged In View This Page...")
        return redirect("home_page")
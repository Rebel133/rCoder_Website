from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<2 or len(phone)<9 or len(content)<5 :
            messages.error(request, 'Please Fill The Form Correctly Before Submiting')
        else:
            messages.success(request, 'We Will Get Back You Soon')
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')


def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    
    if allPosts.count() == 0:
        messages.warning(request, 'No Search Is Found Please Try Diffent key Word')
    params = {'allPosts': allPosts, 'query':query}
    return render(request,'home/search.html',params)

def handleSignup(request):
    if request.method == 'POST':
       #  Get the post parameter
       username = request.POST['username']
       fname = request.POST['fname']
       lname = request.POST['lname']
       Email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2 = request.POST['pass2']

       #checks for errorneous inputs
       if len(username)<5:
          messages.error(request,'Username Should Be Greater Then 5 Character')
          return redirect('/')
       # To Check AlphaNumeric
       if not username.isalnum():
          messages.error(request,'Username Should Only Contain Alpha Numberic Value')
          return redirect('/')

       # passward Should Match
       if pass1 != pass2:
          messages.error(request,'Passward Do Not Match')
          return redirect('/')

       if len(pass1 and pass2)<8 :
          messages.error(request,'Passward Should Be Of 8 Charachter')
          return redirect('/')
       # create the user
       myuser = User.objects._create_user(username, Email, pass1)
       myuser.first_name = fname
       myuser.last_name = lname
       myuser.save()
       messages.success(request, "Account is Created Sucessfully Created On rCoder")
       return redirect('/')

    else:
       return HttpResponse ('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
       
        if user is not None:
            login(request, user)
            messages.success(request,'You Have SuccessFully Login')
            return redirect('/')
        else:
            messages.error(request, 'Ivalid Credentials, Please Try Again')
            return redirect('/')

    return HttpResponse ('404 - Not Found')

def handleLogout(request):
        logout(request)
        messages.success(request,'You Have SuccessFully Logout')
        return redirect('/')
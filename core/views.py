from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User ,auth 
from django.contrib import messages  
from .models import *
from django.contrib.auth.decorators import login_required
from itertools import chain




# Create your views here.

@login_required(login_url='signin')
def index(request):
    if request.user.is_superuser:
        return redirect('admin:index')  # Redirect to the admin panel
    else:
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user = user_object)
        
        user_following_list = []
        feed = []
        user_following = FollowersCount.objects.filter(follower=request.user.username)
        
        for users in user_following:
            user_following_list.append(users.user)
        for usernames in user_following_list:    
            feed_lists = Post.objects.filter(user = usernames)
            feed.append(feed_lists)
           
        feed_list = list(chain(*feed))    
        
        posts = Post.objects.all()
        return render(request, 'index.html', {'user_profile': user_profile,'posts':feed_list})
    
        


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                auth.login(request, user)
                Profile.objects.create(user=user)
                messages.success(request, 'Account created successfully.')
                return redirect('settings')
        else:
            messages.info(request,'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Email or password incorrect')
            return redirect('signin')
    return render(request, 'signin.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def settings(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        bio = request.POST.get('bio')
        location = request.POST.get('location')
        image = request.FILES.get('profile_pic')
        
        if bio:
            user_profile.bio = bio
        if location:
            user_profile.location = location
        if image:
            user_profile.profile_pic = image
            print('image done')
        user_profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('settings')
    
    return render(request, 'setting.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user
        image = request.FILES.get('image_upload')   
        caption = request.POST.get('caption')
        
        new_post = Post.objects.create(user=user, image_url=image ,caption=caption)
        new_post.save()
        return redirect('/')  
    else:
        return redirect('/')
    return HttpResponse('<h1>Upload Post</h1>')

@login_required(login_url='signin')
def like(request):
    user_object = User.objects.get(username=request.user.username)
    post_id = request.GET.get('post_id')
    
    post = Post.objects.get(post_id=post_id)
    
    like_fillter = Like.objects.filter(post_id=post_id, user=user_object).first()
    
    if like_fillter == None:
        new_like = Like.objects.create(user=user_object, post_id =post_id)
        new_like.save()
        
        post.num_likes += 1
        post.save()
        return redirect('/')
    else:
        like_fillter.delete()
        post.num_likes -= 1
        post.save()
        return redirect('/')

@login_required(login_url='signin')    
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=user_object)
    num_posts = len(user_posts)
    
    follower = request.user.username
    username = pk
    user = User.objects.get(username=username)
    if FollowersCount.objects.filter(follower=follower,user=user).first():
        button_text = "Unfollow"
    else:
        button_text = "Follow"
        
    user_followers  = len(FollowersCount.objects.filter(user=user))    
    user_following = len(FollowersCount.objects.filter(follower=pk))
    
    
    context = {
        'user_object': user_object,
        'user_profile':user_profile,
        'user_posts': user_posts,
        'num_posts': num_posts,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, 'profile.html',context)

@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST.get('follower')
        username = request.POST.get('user')
        user = User.objects.get(username=username)
        
        if FollowersCount.objects.filter(follower=follower,user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower,user=user)
            delete_follower.delete()
            return redirect('/profile/' +username)
        else:
            print('----------------------------------------------------')
            new_follower = FollowersCount.objects.create(follower=follower,user=user)
            new_follower.save()
            return redirect('/profile/' +username) 
    else:
        return redirect('/')

@login_required(login_url='signin')            
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        username_object = User.objects.filter(username__icontains=username)
        
        username_profile = []
        username_profile_list = []
        
        for users in username_object:
            username_profile.append(users.id)
        
        for ids in username_profile:  
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        username_profile_list = list(chain(*username_profile_list))    
    return render(request, 'search.html', {'user_profile':user_profile, 'username_profile_list':username_profile_list})

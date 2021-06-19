from random import random
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .models import CustomUser,Category
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm
from .models import Post
from bs4 import BeautifulSoup
from random import sample
import re




def get_cat():
    return Category.objects.all()


def aboutview(request):
    return render(request,'about.html',context={'all_categories':get_cat()})



def homeview(request):
    all_posts=Post.objects.all()
    context={'all_categories':get_cat(),'all_posts':sample(list(all_posts),4)}
    return render(request,'index.html',context=context)

@csrf_exempt
def add_blogview(request):
    return render(request, 'add_blog.html', {'form': PostForm(),'all_categories':get_cat()})

@csrf_exempt
def save_postview(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            note = form.save(commit=False)  
            note.user = request.user
            soup=BeautifulSoup(note.body,'html5lib')
            image=soup.find('img')['src']
            note.thumb_url=image
            note.save()
            return redirect('show_post')
        else:
            return HttpResponse('invalid form')
    else:
        return HttpResponse('invalid request')

def show_postview(request):
    all_posts=Post.objects.all()
    return render(request,'show_post.html',{'all_posts':all_posts[::-1],'all_categories':get_cat()})


def post_detailview(request,posturl):
    if posturl:
        post=Post.objects.filter(slug=posturl).first()
        if post is not None:
            return render(request,'post_detail.html',{'post':post,'all_categories':get_cat()})
        else:
            return HttpResponse('no post found')
    else:
        return HttpResponse('no slug found')


def edit_postview(request,posturl):
    if posturl:
        post=Post.objects.filter(slug=posturl).first()
        form=PostForm(instance=post)
        return render(request,'edit_post.html',{'form':form,'slug':posturl,'all_categories':get_cat()})

def update_postview(request,posturl):
    if request.method =='POST':
        post=Post.objects.filter(slug=posturl).first()
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            note = form.save(commit=False)  
            note.user = request.user
            soup=BeautifulSoup(note.body,'html5lib')
            image=soup.find('img')['src']
            note.thumb_url=image
            note.save()
            return redirect('show_post')
        else:
            return HttpResponse('invalid form')
    else:
        print('HttpResponse')
        return HttpResponse('this is get requestr')

def delete_view(request,posturl):
    try:
        post=Post.objects.get(slug=posturl)
        post.delete()
        return redirect('home')
    except:
        return HttpResponse('404 not found ')



def category_view(request,type):
    categoryname=Category.objects.filter(category=type).first()
    all_posts=Post.objects.filter(category=categoryname)
    return render(request,'show_post.html',{'all_posts':all_posts,'title':type,'all_categories':get_cat()})



@csrf_exempt
def signupview(request, x=None):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email) :
            return HttpResponse(1)
        user_obj = CustomUser.objects.filter(email=email).exists()
        if not user_obj:
            password1 = make_password(password1)
            user = CustomUser.objects.create(first_name=name, email=email, password=password1)
            user.save()
            return HttpResponse(0)
        else:
            return HttpResponse(2)    
    else:
        return HttpResponse('404 not found')


@csrf_exempt
def loginview(request, x=None):
    if request.method == "POST":
        loginusername = request.POST['email']
        loginpassword = request.POST['password']
        usr = authenticate(request, email=loginusername,
                           password=loginpassword)
        if usr is not None:
            login(request, usr)
        else:   
            return HttpResponse(1)
        return HttpResponse(0)
    else:
        return HttpResponse('404 not found!')


def logoutview(request, x=None):
    logout(request)
    return redirect('home')

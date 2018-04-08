from django.views.static import serve
from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from frbblog.models import author,category,article
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(requset):
	post=article.objects.all()
	post_context={
	'post':post
	}
	return render(requset,'index.html',post_context)

def getauthor(requset,name):
	return render(requset,'profile.html')

def getcategory(requset,name):
	singlecategory=get_object_or_404(category,name=name)
	post=article.objects.filter(category=singlecategory.id)
	catpost={
	'post':post,
	'singlecategory':singlecategory
	}
	return render(requset,'category.html',catpost)

def getsinglepost(requset,id):
	post=get_object_or_404(article,pk=id)
	first=article.objects.first()
	last=article.objects.last()
	related=article.objects.filter(category=post.category).exclude(id=id)[:4]
	single_post={
	'post':post,
	'first':first,
	'last':last,
	'related':related
	}
	return render(requset,'single.html',single_post)

def getuserlogin(requset):
	if requset.user.is_authenticated:
		return redirect('index')
	else:
		if requset.method=="POST":
			user=requset.POST.get('name')
			pas=requset.POST.get('password')
			auth=authenticate(requset,username=user,password=pas)
			if auth is not None:
				login(requset,auth)
				return redirect('index')
	return render(requset,'login.html')

def getlogout(requset):
	logout(requset)
	return redirect('index')
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blogs,Category,Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.

def posts_by_category(request,category_id):

    #fetch the posts that belongs to the category with id 

    posts =Blogs.objects.filter(status='published', category = category_id)
    

    #use try when we want to perfrom some action if the category does not exist
    try:
        category=Category.objects.get(pk=category_id)
    except:
        return redirect('home')

    #use get_objec_or_404 if the category does not exist 
    
    category = get_object_or_404(Category,pk=category_id)


    context = {
        'posts':posts,
        'category':category
    }
    
    return render(request, 'posts_by_category.html',context)



#blogs

def blogs(request, slug):
    single_post=get_object_or_404(Blogs,slug=slug,status='published')
    #comment
    if request.method=="POST":
        comment =Comment()
        comment.user=request.user
        comment.blog=single_post
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments=Comment.objects.filter(blog=single_post)
    comment_count=comments.count()

    context={
        'single_post':single_post,
        'comments':comments,
        'comment_count':comment_count
    }
    return render(request,'blogs.html',context)


#seach

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blogs.objects.filter(title__icontains=keyword)
    content={
        'blogs':blogs,
        'keyword':keyword
    }
    
    return render(request,'search.html',content)
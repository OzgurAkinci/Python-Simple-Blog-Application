# -*- coding: utf-8 -*-
from django.shortcuts import render
from BlogApplication.models import Post,Category,Page
from django.core.paginator  import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

# Create your views here.

def HomeView(request):
    page_title = "Home"
    page_slogan = "Blog"
    categories = Category.objects.filter().order_by('-id')
    pages = Page.objects.filter(is_active=True)
    db = Post.objects.filter(is_active=True).order_by('-id')[:5]
    #Pagination
    paginator = Paginator(db, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        db = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        db = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        db = paginator.page(paginator.num_pages)
    #!Pagination
    context = {
    'db': db,
    'pages': pages,
    'categories' : categories,
    'page_title': page_title,
    'page_slogan': page_slogan,
    }
    return render(request, 'Home.html', context)

def PostView(request,seo_url):
    pages = Page.objects.filter(is_active=True)
    single_post = Post.objects.filter(seo_url=seo_url)
    post_title = single_post[0].title
    page_slogan = "Blog"
    categories = Category.objects.filter().order_by('-id')
    context = {
    'page_title': post_title,
    'page_slogan': page_slogan,
    'pages': pages,
    'categories' : categories,
    'single_post': single_post,
    }
    return render(request, 'Post.html', context)

def PageView(request,seo_url):
    pages = Page.objects.filter(is_active=True)
    single_page = Page.objects.filter(seo_url=seo_url)
    page_title = single_page[0].title
    page_slogan = "Blog"
    categories = Category.objects.filter().order_by('-id')
    context = {
    'pages': pages,
    'page_title': page_title,
    'page_slogan': page_slogan,
    'categories' : categories,
    'single_page': single_page,
    }
    return render(request, 'Page.html', context)

def CategoryView(request,seo_url):
    categories = Category.objects.filter().order_by('-id')
    #get posts in selected category
    selected_category = Category.objects.get(seo_url=seo_url)
    selected_posts = Post.objects.filter(category_list_id=selected_category.id).order_by('-id')[:5]
    #!get posts in selected category
    page_slogan = "Blog"
    pages = Page.objects.filter(is_active=True)
    #Pagination
    paginator = Paginator(selected_posts, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        selected_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        selected_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        selected_posts = paginator.page(paginator.num_pages)
    #!Pagination
    context = {
    'db': selected_posts,
    'pages': pages,
    'category_name': selected_category.category_name,
    'categories' : categories,
    'page_title': selected_category.category_name,
    'page_slogan': page_slogan,
    }
    return render(request, 'Category.html', context)

def SearchView(request):
    q = request.GET.get('q')
    #get posts in search parameter
    selected_posts = Post.objects.filter(Q(title__icontains=q))

    categories = Category.objects.filter().order_by('-id')
    pages = Page.objects.filter(is_active=True)
    #Pagination
    paginator = Paginator(selected_posts, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        selected_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        selected_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        selected_posts = paginator.page(paginator.num_pages)
    #!Pagination
    page_slogan = "Blog"
    context = {
    'db': selected_posts,
    'pages': pages,
    'categories' : categories,
    'page_title': q,
    'page_slogan': page_slogan,
    }
    return render(request, 'Search.html', context)

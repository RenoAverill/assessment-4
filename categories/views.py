from .models import Category, Post
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import CategoryForm, PostForm
# Create your views here.

# helper methods


def get_category(category_id):
    return Category.objects.get(id=category_id)


def get_post(post_id):
    return Post.objects.get(id=post_id)


# category methods
def category_list(request):
    categories = Category.objects.all()
    return render(request, "my_pages/category_list.html", {"categories": categories})


def category_detail(request, category_id):
    category = get_category(category_id)
    return render(request, "my_pages/category_detail.html", {"category": category})


def category_new(request):
    form = CategoryForm(request.POST or None)

    if request.method == 'POST':
        try:
            form.save()
            return redirect('category_list')
        except:
            return HttpResponse("ERROR Creating Category!")

    data = {'form': form, 'create_or_update': True}

    return render(request, 'my_pages/category_form.html', data)


def category_edit(request, category_id):
    try:
        category = get_category(category_id)
    except:
        print('error')
        return HttpResponse("That Category doesn't exist!")

    form = CategoryForm(request.POST, instance=category)

    if request.method == 'POST':
        try:
            form.save()
            return redirect('category_detail', category_id=category.id)
        except Exception as e:
            print(e)
            return HttpResponse("ERROR Updating Category!")

    data = {'form': form, 'create_or_update': False}

    return render(request, 'my_pages/category_form.html', data)


def category_delete(request, category_id):
    if request.method == "POST":
        category = get_category(category_id)
        category.delete()
    return redirect('category_list')


# Post Methods

def post_list(request, category_id):
    category = get_category(category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'my_pages/post_list.html', {'category': category, 'posts': posts})


def post_new(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_detail', category_id=post.category.id, post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'my_pages/post_form.html', {'form': form, 'type_of_request': 'New'})


def post_detail(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    return render(request, 'my_pages/post_detail.html', {'category': category, 'post': post})


def post_edit(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post.id, category_id=category.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'type_of_request': 'Edit'})


def post_delete(request, category_id, post_id):
    if request.method == "POST":
        post = get_post(post_id)
        post.delete()
    return redirect('post_list', category_id=category_id)

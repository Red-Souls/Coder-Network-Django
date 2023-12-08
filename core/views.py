from django.shortcuts import render, redirect
from .forms import*
from django.views.generic import CreateView

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-date')
    recentPosts = Post.objects.all().order_by('-date')[0:5]
    return render(request, 'core/index.html', {
        'posts': posts,
        'recentPosts': recentPosts,
    })

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            profile = Profile()
            profile.user = form.save()
            profile.userId = form.save().id
            profile.save()
            return redirect('/signin/')
    return render(request, 'core/signup.html', {
        'form': form,
    })

def profile(request, id):
    requestProfile = Profile.objects.get(userId = id)
    posts = Post.objects.filter(authorProfile = requestProfile)
    return render(request, 'core/profile.html', {
        'profile': requestProfile,
        'posts': posts,
    })

def detail(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post = id).order_by('-date')
    form = CommentPostForm()
    if not request.user.is_anonymous:
        userProfile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = CommentPostForm(request.POST)
        form.instance.author = request.user
        form.instance.authorProfile = userProfile
        form.instance.post = post;
        if form.is_valid():
            form.save()
            return redirect('/post/{}/'.format(id))
    return render(request, 'core/detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

def postUpload(request):
    form = PostUploadForm()
    userProfile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = PostUploadForm(request.POST, request.FILES)
        form.instance.author = request.user
        form.instance.authorProfile = userProfile
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'core/upload.html', {
        'form': form,
    })

def postUpdate(request, id):
    post = Post.objects.get(id = id)
    form = PostUpdateForm()
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            post.title = request.POST['title']
            post.content = request.POST['content']
            if request.FILES:
                post.headerImg = request.FILES['headerImg']
            post.save()
            return redirect('/post/{}/'.format(id))
    return render(request, 'core/update.html', {
        'post': post,
        'form': form,
    })

def postDelete(request, id):
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'core/delete.html', {
        'post': post,
    })

def profileUpdate(request, id):
    requestProfile = Profile.objects.get(userId = id)
    form = ProfileUpdateForm()
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            requestProfile.description = request.POST['description']
            if request.FILES:
                requestProfile.image = request.FILES['image']
            requestProfile.save()
            return redirect('/profile/{}/'.format(id))
    return render(request, 'core/updateProfile.html', {
        'profile': requestProfile,
        'form': form,
    })

def commentDelete(request, id):
    comment = Comment.objects.get(id = id)
    postId = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return redirect('/post/{}/'.format(postId))
    return render(request, 'core/deleteComment.html', {
        'comment': comment,
    })

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from hair.forms import PostForm, CommentForm, InspireUserCreationForm
from hair.models import Post, Categories, Comment


def register(request):
    if request.method == 'POST':
        form = InspireUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.email_user("Welcome!", "Welcome to inspiration.com,  is added to one of your posts")
            return redirect('home')
    else:
        form = InspireUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = request.user
            body = form.cleaned_data['body']
            category = form.cleaned_data['category']
            Post.objects.create(category=category, body=body, author=author, title=title)
            return redirect('home')
    else:
        form = PostForm()
    return render(request, "post.html", {'form': form})

def music(request):
    great = Post.objects.filter(category__name="Music")
    return render(request, "music.html", {'great': great})

def view_music_post(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {"post": post}
    return render(request, "music/view_music_post.html", data)

def view_acting_post(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {"post": post}
    return render(request, "acting/view_acting_post.html", data)

def view_medicine_post(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {"post": post}
    return render(request, "medicine/view_medicine_post.html", data)

def view_programming_post(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {"post": post}
    return render(request, "music/view_programming_post.html", data)

def view_sports_post(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {"post": post}
    return render(request, "sports/view_sports_post.html", data)

def view_law_post(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {"post": post}
    return render(request, "music/view_music_post.html", data)

def profile(request):
    return render(request, 'profile.html')

def home(request):
    post = Post.objects.all()
    return render(request, 'home.html', {'post': post})

def about(request):
    return render(request, 'about.html', )

def faq(request):
    return render(request, 'faq.html', )

def medicine(request):
    great = Post.objects.filter(category__name="Medicine")
    return render(request, "medicine.html", {'great': great})

def law(request):
    great = Post.objects.filter(category__name="Law")
    return render(request, "law.html", {'great': great})

def acting(request):
    great = Post.objects.filter(category__name="Acting")
    return render(request, "acting.html", {'great': great})

def sports(request):
    great = Post.objects.filter(category__name="Sports")
    return render(request, "sports.html", {'great': great})

def programming(request):
    great = Post.objects.filter(category__name="Programming")
    return render(request, "programming.html", {'great': great})

def edit(request):
    set = Post.objects.all()

    return render(request, 'edit.html', {'set': set})

# def view_profile(request, username):
#    user_id = request.user
#    profile = Profile.objects.get(user=user_id)
#    first_name = profile.first_name
#    last_name = profile.last_name
#    bio = profile.bio
#    if not profile.avatar:
#        avatar = "/media/avatar/default_avatar.jpg"
#        print avatar
#    else:
#        avatar = profile.avatar.url
#    #avatar = profile.avatar.url #this is a string avatar/60818_10201083718174136_4635851443860706305_n_1.jpg
#    #print avatar
#    data = {'first_name':first_name,'last_name':last_name, 'bio':bio, 'avatar':avatar, 'username':username}
#    return render(request, "profile.html", data)


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F
from django.shortcuts import render, redirect

from todolist_app.forms import AuthenticateForm, TaskBox, UserCreateForm
from todolist_app.models import Task, UserProfile


def index(request, auth_form=None, user_form=None):
    if request.user.is_authenticated():
        task_box = TaskBox()
        tasks = Task.objects.select_related('user__profile').order_by('-rank').all()
        points = request.user.profile.wish_points
        image = request.user.profile.image
        return render(request,
                      'logged.html', {'task_box': task_box, 'tasks': tasks, 'username': request.user.username,
                                      'points': points, 'image': image})
    else:
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()

        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        else:
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


def create_all_related_user_models(user):
    UserProfile.objects.create(user=user)
    return


def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password2']
            user_form.save()
            user = authenticate(username=username, password=password)
            create_all_related_user_models(user)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')

@login_required
def submit(request):
    if request.method == "POST":
        task_box = TaskBox(data=request.POST)
        if task_box.is_valid():
            task = task_box.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')


@login_required
def vote_up(request, wish_id):
    wish = Task.objects.get(id=wish_id)
    wish.rank += 1
    wish.save()
    user = UserProfile.objects.get(user=request.user.id)
    user.wish_points -= 1
    user.save()
    return redirect('/')


@login_required
def vote_down(request, wish_id):
    wish = Task.objects.get(id=wish_id)
    wish.rank -= 1
    wish.save()
    user = UserProfile.objects.get(user_id=request.user.id)
    user.wish_points -= 1
    user.save()
    return redirect('/')


@login_required
def increase_points(request, user_id):
    increase = UserProfile.objects.filter(user_id=user_id)
    increase.update(wish_points=F('wish_points')+5)
    return redirect('/')
    # increase = UserProfile.objects.get(user_id=user_id)
    # increase.wish_points += 5
    # increase.save()
    # return redirect('/')



@login_required
def get_user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    tasks = Task.objects.filter(user_id=user_id)
    return render(request, 'user.html', {'user': user, 'tasks': tasks,
                                         'username': request.user.username,
                                         'image': request.user.profile.image,
                                         'points': request.user.profile.wish_points})

@login_required
def delete(request, wish_id):
    obj = Task.objects.get(id=wish_id)
    obj.delete()
    return redirect('/')


# def upload_pic(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = Task.objects.get(user_id=user_id)
#             m.model_pic = form.cleaned_data['image']
#             m.save()
#             return redirect('/')
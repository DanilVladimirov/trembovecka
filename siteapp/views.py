import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from siteapp.models import *
from siteapp.forms import PostPhotoForm, UserRegisterForm
from django.core.mail import send_mail
from trembovetska.settings import EMAIL_HOST_USER


def main_page(request):
    context = {}
    text_main = StartPage.objects.filter()
    if text_main.exists():
        context = {'text_main': text_main[0]}
    return render(request, 'main-page.html', context)


def create_post(request):
    data_response = {}
    if request.POST:
        post = Post.objects.create(title=request.POST.get('title'),
                                   text=request.POST.get('text'))
        post.save()
        data_response.update({'title': post.title, 'text': post.text, 'pid': post.id})
        form_photo = PostPhotoForm(request.POST, request.FILES, instance=post)
        if form_photo.is_valid():
            form_photo.save()
        if post.photo:
            data_response.update({'success': True, 'photo': post.photo.url})
        else:
            data_response.update({'success': False})
    return HttpResponse(json.dumps(data_response), content_type='application/json')


def del_post(request):
    data_response = {}
    if request.POST:
        post = Post.objects.get(id=request.POST.get('post_id'))
        post.delete()
        data_response.update({'success': True})
    return HttpResponse(json.dumps(data_response), content_type='application/json')


def contact_page(request):
    context = {}
    dates = ConsultationDate.objects.all()

    context.update({'dates': dates})
    return render(request, 'contact.html', context)


def register_cons(request):
    data_responce = {}
    if request.POST:
        date = ConsultationDate.objects.get(id=request.POST.get('date'))
        group = request.POST.get('group')
        full_name = request.POST.get('full_name')
        email = request.POST.get('mail')
        send_mail(f'{full_name} {group} записався на консультацію',
                  f'{full_name} записався на {date.day}-{date.time}, його пошта: {email}',
                  EMAIL_HOST_USER,
                  ['danilvladimirovnkk@gmail.com'],
                  fail_silently=True)
        data_responce.update({'success': True})
    return HttpResponse(json.dumps(data_responce), content_type='application/json')


@login_required(login_url='login_page')
def files_page(request):
    context = {}
    categories = Category.objects.all()
    context.update({'categories': categories})
    return render(request, 'files-page.html', context)


@login_required(login_url='login_page')
def category_page(request, cid):
    context = {}
    files = Category.objects.get(id=cid).files.all()
    context = {'files': files}
    return render(request, 'category-page.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
    return render(request, 'login-page.html')


def logout_page(request):
    logout(request)
    return redirect('main_page')


def registration_page(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        print(form.errors)
    return render(request, 'register-page.html')


def forum_page(request):
    themes = Theme.objects.order_by('-id')
    context = {'themes': themes}
    if request.POST:
        q = request.POST.get('q')
        themes = Theme.objects.filter(title__icontains=q)
        context = {'themes': themes}
    return render(request, 'forum-page.html', context)


@login_required(login_url='login_page')
def forum_create_theme(request):
    if request.POST:
        title = request.POST.get('title')
        text = request.POST.get('text')
        new_theme = Theme.objects.create(title=title,
                                         text=text,
                                         author=request.user)
        new_theme.save()
        return redirect('forum_theme', theme_id=new_theme.id)
    return render(request, 'theme-create.html')


def forum_theme(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    context = {'theme': theme}
    if request.POST:
        text = request.POST.get('text')
        new_message = Message.objects.create(text=text,
                                             author=request.user)
        new_message.save()
        theme.message.add(new_message)
    return render(request, 'theme-page.html', context)


def news_page(request):
    context = {}
    posts = Post.objects.order_by('-id')
    context.update({'posts': posts})
    return render(request, 'news-page.html', context)


def about_group(request):
    context = {}
    group = GroupPage.objects.filter()
    if len(group) >= 1:
        context.update({'group': group[0]})
    achivements = Post.objects.filter(type_post='achive')
    context.update({'posts': achivements})

    return render(request, 'group-page.html', context)

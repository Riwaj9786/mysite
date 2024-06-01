from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from rioz.models import Information, About, Experience, Service, Skills, Clients, Message, Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from rioz.forms import MessageForm, ResumeForm, Info_EditForm, About_EditForm, Client_Form

# Create your views here.
def home(request):
    information = Information.objects.first()
    about = About.objects.first()
    service = Service.objects.all()
    skills = Skills.objects.all().order_by('skill_name')
    return render(request, 'rioz/about.html', {'information': information,
                                               'about': about,
                                               'services': service,
                                               'skills': skills})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('rioz:home'))
            else:
                return HttpResponseRedirect('Account not Active!')
            
        else:
            print("Unauthorized Login!")

    else:
        return render(request, 'rioz/login.html')
    

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('rioz:home'))



@login_required
def message_user(request):
    information = Information.objects.first()
    about = About.objects.first()
    message = Message.objects.all().order_by('-send_time')

    return render(request, 'rioz/message_user.html', {'information': information,
                                                      'about': about,
                                                      'messages': message})


@login_required
def messages_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()

    return redirect('rioz:messages')




def blog(request):
    blog = Blog.objects.all()
    information = Information.objects.first()
    about = About.objects.first()

    return render(request, 'rioz/blog_page.html', {'blog': blog,
                                                   'information': information,
                                                   'about': about})




def messageForm(request):
    information = Information.objects.first()
    about = About.objects.first()

    if request.method == 'POST':
        message_form = MessageForm(data = request.POST)

        if message_form.is_valid():
            message = message_form.save(commit=True)
            message.save()

        else:
            messages.info('The message is not Sent.')

        return redirect('rioz:message_form')
    else:
        message_form = MessageForm()
        return render(request, 'rioz/contact.html', {'information': information,
                                                    'about': about,
                                                    'message_form': message_form})
    


def resume_view(request):
    information = Information.objects.first()
    about = About.objects.first()

    if request.method == "POST":
        resume_form = ResumeForm(request.POST, request.FILES)

        if resume_form.is_valid():
            resume_form.save(commit=True)
            messages.success(request, "New CV Added Successfully!")
            return redirect('rioz:resume')
        else:
            messages.error(request, "Upload Error!")
            return redirect('rioz:resume')

    else:
        resume_form = ResumeForm()

    return render(request, 'rioz/resume.html', {'information': information,
                                                'form': resume_form,
                                                'about': about,})




def experience_view(request):
    experience = Experience.objects.all().order_by('is_complete', '-end_date', 'start_date')
    information = Information.objects.first()
    about = About.objects.first()
    client = Clients.objects.all().order_by('client_name')

    if request.method == "POST":
        client_form = Client_Form(request.POST, request.FILES)

        if client_form.is_valid():
            client_form.save(commit=True)
            messages.success(request, "Client Added Successfully!")
            return redirect('rioz:experience')

        else:
            messages.error(request, "Client is not Added!")
            return redirect("rioz:experience")
        
    else:
        client_form = Client_Form()

    return render(request, "rioz/experience.html", {'information': information,
                                                    'experience': experience,
                                                    'about': about,
                                                    'clients': client,
                                                    'form': client_form})


@login_required
def edit_information_about(request):
    information = get_object_or_404(Information, id=1)  # Assuming there's only one instance
    about = get_object_or_404(About, id=1)  # Assuming there's only one instance

    if request.method == 'POST':
        info_form = Info_EditForm(request.POST, request.FILES, instance=information)
        about_form = About_EditForm(request.POST, instance=about)
        
        if info_form.is_valid() and about_form.is_valid():
            info_form.save()
            about_form.save()
            messages.success(request, 'Information updated successfully!')
            return redirect('rioz:about')  # Replace with the appropriate view name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        info_form = Info_EditForm(instance=information)
        about_form = About_EditForm(instance=about)

    return render(request, 'edit_information_about.html', {
        'info_form': info_form,
        'about_form': about_form,
        'information': information,
        'about': about
    })


@login_required
def client_manage(request):
    information = Information.objects.first()
    about = About.objects.first()
    clients = Clients.objects.all().order_by('client_name')

    return render(request, 'rioz/client_manage.html', {'information': information,
                                                       'about': about,
                                                       'clients': clients})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Clients, pk=pk)
    client.delete()

    return redirect('rioz:experience')
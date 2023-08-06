from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import Event, EventRegistration
from django.utils import timezone
from django.contrib.auth.decorators import login_required

#@login_required(login_url='login')
def event_list(request):
    upcoming_events = Event.objects.filter(start_date__gte=timezone.now())
    past_events = Event.objects.filter(end_date__lt=timezone.now())
    upcoming_count= upcoming_events.count()
    past_count= past_events.count()
    return render(request, 'home/event_list.html', {'upcoming_events': upcoming_events, 'past_events': past_events, 'upcoming_count':upcoming_count, 'past_count':past_count})
#@login_required(login_url='login')
def event_detail(request, event_id):
    events= Event.objects.all()
    event = Event.objects.get(id=event_id)
    registered_users = EventRegistration.objects.filter(event=event)
    paid_users = registered_users.filter(is_paid=True)
    unpaid_users = registered_users.filter(is_paid=False)
    return render(request, 'home/event_detail.html', {'event': event, 'registered_users': registered_users, 'paid_users': paid_users, 'unpaid_users': unpaid_users, 'events':events})


#def event_registration(request, event_id):
    #event = get_object_or_404(Event, id=event_id)
    
    #if request.method == 'POST':
        #is_paid = request.POST.get('is_paid', False)
        #user = request.user
        #EventRegistration.objects.create(event=event, user=user, is_paid=is_paid)
        #return redirect('event_detail', event_id=event.id)

    #return render(request, 'home/event_registration.html', {'event': event})
#@login_required(login_url='login')
def event_registration(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            event = form.cleaned_data['event']
            user = form.cleaned_data['user']
            email = form.cleaned_data['email']
            
            
        
            EventRegistration.objects.create(event=event, user=user, email=email)
            return redirect('event_detail', event= event)
    else:
        form = EventRegistrationForm()

    return render(request, 'home/event_registration.html', {'event': event, 'form': form})
#@login_required(login_url='login')
def home(request):
    events= Event.objects.all()
    total_events= events.count()
    upcoming_events = Event.objects.filter(start_date__gte=timezone.now())
    past_events = Event.objects.filter(end_date__lt=timezone.now())
    upcoming_count= upcoming_events.count()
    past_count= past_events.count()
    return render(request,'home/dashboard.html', {'upcoming_events': upcoming_events, 'past_events': past_events, 'upcoming_count':upcoming_count, 'past_count':past_count, 'events':events, 'total_events': total_events})

#@login_required(login_url='login')
def payment(request):
    return render(request,'home/payment.html')


def organizer_registration(request):
    if request.user.is_authenticated:
       return redirect('home')
    else:
        if request.method == 'POST':
            form = OrganizerRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                Organizer.objects.create(user=user)
                messages.success(request, 'Account was created ')
                return redirect('login')
        else:
            form = OrganizerRegistrationForm()
        return render(request, 'home/organizer_registration.html', {'form': form})

def client_registration(request):
    if request.user.is_authenticated:
       return redirect('home')
    else:
        if request.method == 'POST':
            form = ClientRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                Client.objects.create(user=user)
                messages.success(request, 'Account was created')
                return redirect('login')
        else:
            form = ClientRegistrationForm()
        return render(request, 'home/client_registration.html', {'form': form})

#def registerPage(request):
   #if request.user.is_authenticated:
      #return redirect('home')
   #else:
       # form= CreateUserForm()
        #if request.method=='POST':
           # form= CreateUserForm(request.POST)
           # if form.is_valid():
               # form.save()
               # user= form.cleaned_data.get('username')
               # messages.success(request, 'Account was created for '+ user)
               # return redirect('login')
        #context={'form':form}
        #return render(request, 'home/register.html', context)
    
def loginPage(request):
   if request.user.is_authenticated:
       return redirect('home')
   else:
        if request.method =='POST':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user =authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
            
        context={}
        return render(request, 'home/login.html', context)
    
def logoutUser(request):
    logout(request)
    return redirect('login')

#def createEvent(request,pk):
    #form= CreateEvent()
   # organizer= Organizer.objects.get(id=pk)


   # if request.method=='POST':
        #form= CreateEvent(request.POST, instance=organizer)
        #if form.is_valid():
            #form.save()
            #return redirect('/')
        
   # context={'form': form,'organizer':organizer}
   # return render(request, 'home/create_event.html', context)
#@login_required(login_url='login')
def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list') 
    else:
        form = EventCreationForm()

    return render(request, 'home/create_event.html', {'form': form})


#@login_required(login_url='login')
def event_feedback(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventFeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            rating = form.cleaned_data['rating']
            feedback = form.cleaned_data['feedback']

            EventFeedback.objects.create(event=event, name=name, email=email, rating=rating, feedback=feedback)
            return render(request, 'home/feedback_success.html', {'event': event})
    else:
        form = EventFeedbackForm()

    return render(request, 'home/feedback.html', {'event': event, 'form': form})


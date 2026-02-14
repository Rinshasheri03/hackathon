from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import SkillPost, Message, Profile
from .forms import SkillForm
from django.contrib.auth.forms import UserCreationForm

# ---------------- Authentication Views ----------------

# Register View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from core.models import Profile
# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import Profile

# core/views.py
# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from core.models import Profile

# Registration view
# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from core.models import Profile

def register_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        email = request.POST['email'].strip()
        full_name = request.POST['full_name'].strip()
        department = request.POST.get('department', '').strip()
        college = request.POST.get('college', '').strip()
        year = request.POST.get('year', '').strip()

        # Unique checks
        if User.objects.filter(username=username).exists():
            context['error'] = "Username already exists. Please choose another."
            return render(request, 'register.html', context)
        if User.objects.filter(email=email).exists():
            context['error'] = "Email already registered. Please login."
            return render(request, 'register.html', context)

        # Create user (Profile auto-created by signal)
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=full_name
        )

        # Update profile details
        profile = user.profile
        profile.department = department or None
        profile.college = college or None
        profile.year = int(year) if year else None
        profile.save()

        # Redirect directly to login page
        return redirect('login')

    return render(request, 'register.html', context)

def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            context['login_error'] = "Invalid username or password."
            context['username'] = username

    return render(request, 'login.html', context)

@login_required
def home_view(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            context['login_error'] = "Invalid username or password."
            context['username'] = username

    return render(request, 'login.html', context)

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            # If user doesn't exist, redirect to register
            messages.error(request, "No account found! Please register first.")
            return redirect("register")

    return render(request, "login.html")


# Logout View
def logout_view(request):
    logout(request)
    return redirect("login")


# ---------------- Static Page Views ----------------

def home(request):
    return render(request, "home.html")


# ---------------- Skill Posting ----------------

@login_required
def tech_page(request):
    created_skill = None
    chat_messages = []

    if request.method == "POST":
        # Posting the skill
        topic = request.POST.get('topic')
        description = request.POST.get('description')
        video_file = request.FILES.get('video_file')

        created_skill = SkillPost.objects.create(
            teacher=request.user,
            topic=topic,
            description=description,
            video=video_file
        )

    # If a new skill was created, load its messages
    if created_skill:
        chat_messages = Message.objects.filter(skill=created_skill).order_by('timestamp')

    # Handle chat message submission (same view)
    if request.method == "POST" and request.POST.get('message'):
        message_text = request.POST.get('message')
        if message_text and created_skill:
            Message.objects.create(
                skill=created_skill,
                sender=request.user,
                text=message_text
            )
            return redirect('tech')

    return render(request, "tech.html", {
        "created_skill": created_skill,
        "messages": chat_messages
    })


# Learn Page
def learn_page(request):
    skills = SkillPost.objects.all().order_by('-uploaded_at')
    return render(request, 'learn.html', {'skills': skills})


# Skill Detail (for learners)
@login_required
def skill_detail(request, skill_id):
    skill = get_object_or_404(SkillPost, id=skill_id)
    chat_messages = Message.objects.filter(skill=skill).order_by('timestamp')

    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            Message.objects.create(
                skill=skill,
                sender=request.user,
                text=message_text
            )
        return redirect('skill_detail', skill_id=skill.id)

    return render(request, 'skill_detail.html', {
        'skill': skill,
        'messages': chat_messages
    })


# ---------------- Teacher Only Views ----------------

@login_required
def skill_detail_teacher(request, pk):
    skill = get_object_or_404(SkillPost, id=pk)

    # Only allow teacher to view this
    if request.user != skill.teacher:
        return redirect('learn')

    # Fetch chat messages
    chats = Message.objects.filter(skill=skill).order_by('timestamp')

    if request.method == "POST":
        message_text = request.POST.get('message')
        if message_text:
            Message.objects.create(
                skill=skill,
                sender=request.user,
                text=message_text
            )
        return redirect('skill_detail_teacher', pk=skill.id)

    return render(request, "skill_detail_teacher.html", {
        "skill": skill,
        "messages": chats
    })


@login_required
def edit_skill(request, pk):
    skill = get_object_or_404(SkillPost, id=pk)

    if request.user != skill.teacher:
        return redirect('learn')

    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_detail_teacher', pk=skill.id)
    else:
        form = SkillForm(instance=skill)

    return render(request, "edit_skill.html", {"form": form})

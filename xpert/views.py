from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectsForm, ServicesForm, ReviewsForm, ServiceSearchForm
from xpert_users.forms import UserRegistrationForm, UserProfileForm
from .models import Projects, Service, Reviews
from xpert_users.models import User
from django.contrib import messages
# Create your views here.

def homepage(request):
    """returns the web app home page"""
    profiles = User.objects.all()
    services = Service.objects.all()
    context = {
        'profiles': profiles,
        'services': services,
        }
    return render(request, 'xpert/home.html', context)

# @login_required
# def login_check(request):
#     """checks client login and redirects them accordingly"""
#     user = request.user
#     if user.account_type == "Service provider":
#         return redirect('dashboard')
#     elif user.account_type == "Service seeker":
#         return redirect('home')

@login_required
def dashboard(request):
    """user dashboard"""
    return render(request, 'xpert_users/dashboard.html')


# READ ALL
def all_profiles(request):
    """lists all user profiles from the database"""
    profiles = User.objects.all()
    context = {
        'profiles': profiles,
        }
    return render(request, 'xpert/profiles.html', context)

def all_projects(request):
    """lists all user projects from the database"""
    projects = Projects.objects.all()
    context = {
        'projects': projects,
        }
    
    
    return render(request, 'xpert/projects.html', context)

def all_services(request):
    """lists all user services from the database"""
    services = Service.objects.all()
    context = {
        'services': services,
        }
    return render(request, 'xpert/services.html', context)

def all_reviews(request):
    """lists all user profiles from the database"""
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
        }
    return render(request, 'xpert/reviews.html', context)

# READ ALL BY USER
def all_user_projects(request, id):
    """lists all projects from the database for a given user"""
    profile = User.objects.get(pk=id)
    projects = Projects.objects.filter(provider=profile)
    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'xpert/all_user_projects.html', context)

def all_user_services(request, id):
    """lists all services from the database for given profile"""
    profile = User.objects.get(pk=id)
    services = Service.objects.filter(provider=profile)
    context = {
        'profile': profile,
        'service': services,
    }
    return render(request, 'xpert/all_user_services.html', context)

def all_user_reviews(request, id):
    """lists all reviews from the database for a given user profile"""
    profile = User.objects.get(pk=id)
    reviews = Reviews.objects.filter(provider=profile)
    context = {
        'profile': profile,
        'reviews': reviews,
    }
    return render(request, 'xpert/all_user_reviews.html', context)


# READ INDIVIDUAL
def profile_detail(request, id):
    """displays user profiles for each user"""
    user = User.objects.get(pk=id)
    projects = Projects.objects.filter(provider=user)
    services = Service.objects.filter(provider=user)

    context = {
        'user': user,
        'projects': projects,
        'services': services,
               }

    return render(request, 'xpert/profile_detail.html', context)

def project_detail(request, id):
    """retrieves each project by project id"""
    user = User.objects.get(pk=id)
    project = Projects.objects.get(pk=id)
    context = {
        'user': user,
        'project': project,
    }
    return render(request, 'xpert/project_detail.html', context)

def service_detail(request, id):
    """retrieves each service by service id"""
    service = Service.objects.get(pk=id)
    context = {
        'service': service,
    }

    return render(request, 'xpert/service_detail.html', context)

def review_detail(request, id):
    """retrieves each service by service id"""
    review = Reviews.objects.get(pk=id)
    context = {
        'review': review,
    }

    return render(request, 'xpert/review_detail.html', context)


# CREATE
@login_required
def create_profile(request):
    """creates user account profile"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            profile = form.cleaned_data.get("username")
            messages.success(request, f"Profile created for {profile}")
            return redirect('profile_detail')
    else:
        form = UserProfileForm()

    context = {
        "form": form,
    }

    return render(request, 'xpert/create_profile.html', context)

@login_required
def create_project(request):
    """Adds a new project to user profile"""
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            project = form.cleaned_data.get('project_name')
            messages.success(request, f"{project} has been successfully created!")
            return redirect("user_db_projects", request.user.id) # to user projects
    else:
        form = ProjectsForm()

    context = {
        "form": form,
    }

    return render(request, 'xpert/create_project.html', context)

@login_required
def create_service(request):
    """Adds services the service provider offers"""
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            service =  form.cleaned_data.get("service_name")
            messages.success(request, f"{service} has been successfully created!")
            return redirect("user_db_services", request.user.id)
    else:
        form = ServicesForm()

    context = {
        "form": form,
    }

    return render(request, 'xpert/create_service.html', context)

@login_required
def create_review(request):
    """Adds services the service provider offers"""
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            project = form.cleaned_data.get('project_name')
            messages.success(request, f"Review done for '{project}' project!")
            return redirect("home")
    else:
        form = ReviewsForm()

    context = {
        "form": form,
    }

    return render(request, 'xpert/create_review.html', context)


# UPDATE
@login_required
def update_user(request, id):
    """updates user information in the database"""
    user = User.objects.get(pk=id)

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} account updated successfully")
            return redirect('profile_detail', id=id)
    else:

        form = UserRegistrationForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'xpert/update_user.html', context)

@login_required
def update_profile(request, id):
    """updates user information in the database"""
    profile = User.objects.get(pk=id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "User Account profile updated successfully")
            return redirect('profile_detail', id=id)
    else:

        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'xpert/update_profile.html', context)

@login_required
def update_project(request, id):
    """updates user information in the database"""
    project = Projects.objects.get(pk=id)

    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            project_name = form.cleaned_data.get("project_name")
            messages.success(request, f"{project_name} updated successfully")
            return redirect('project_detail', id=id)
    else:

        form = ProjectsForm(instance=project)

    context = {
        'form': form,
    }

    return render(request, 'xpert/update_project.html', context)

@login_required
def update_service(request, id):
    """updates user information in the database"""
    service = Service.objects.get(pk=id)

    if request.method == 'POST':
        form = ServicesForm(request.POST, instance=service)

        if form.is_valid():
            form.save()
            service_name = form.cleaned_data.get("service_name")
            messages.success(request, f"{service} updated successfully")
            return redirect('service_detail', id=id)
    else:

        form = ServicesForm(instance=service)

    context = {
        'form': form,
    }

    return render(request, 'xpert/update_service.html', context)

@login_required
def update_review(request, id):
    """updates user information in the database"""
    review = Reviews.objects.get(pk=id)

    if request.method == 'POST':
        form = ReviewsForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully")
            return redirect('review_detail', id=id)
    else:

        form = ReviewsForm(instance=review)

    context = {
        'form': form,
    }

    return render(request, 'xpert/update_review.html', context)


# DELETE
@login_required
def delete_user(request, id):
    """Deletes a given user object from the database"""
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User successfully deleted.")
        return redirect('profiles')

    context = {
        'user': user,
    }
    return render(request, 'xpert/delete_user.html', context)

@login_required
def delete_profile(request, id):
    """Deletes a given user object from the database"""
    profile = User.objects.get(pk=id)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, "User profile successfully deleted.")
        return redirect('profiles')

    context = {
        'profile': profile,
    }
    return render(request, 'xpert/delete_profile.html', context)

@login_required
def delete_project(request, id):
    """deletes a given project object from the database"""
    project =  Projects.objects.get(pk=id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect('projects')

    context = {
        'project': project,
    }

    return render(request, 'xpert/delete_project.html', context)

@login_required
def delete_service(request, id): # TO BE FIXED
    """deletes a given service object from the database"""
    service = Service.objects.get(pk=id)

    if request.method == "POST":
        service.delete()
        messages.success(request, "Service deleted successfully!")
        return redirect('services')
    context = {
        'service': service,
    }

    return render(request, 'xpert/delete_service.html', context)

@login_required
def delete_review(request, id):
    """deletes a given review object from the database"""
    review = Reviews.objects.get(pk=id)

    if request.method == "POST":
        review.delete()
        messages.success(request, "Review deleted successfully!")
        return redirect('reviews')

    context = {
        'review': review,
    }

    return render(request, 'xpert/delete_review.html', context)



# CLIENT DASHBOARD

def all_user_db_services(request, id):
    """lists all services from the database for given profile"""

    profile = User.objects.get(pk=id)
    services = Service.objects.filter(provider=profile)
    context = {
        'profile': profile,
        'services': services,
    }
    return render(request, 'xpert_users/all_user_db_services.html', context)

def all_user_db_projects(request, id):
    """lists all projects from the database for a given user"""
    profile = User.objects.get(pk=id)
    projects = Projects.objects.filter(provider=profile)
    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'xpert_users/all_user_db_projects.html', context)

# ADMIN DASHBOARD

def all_users_db_profiles(request):
    """lists all user profiles from the database"""
    profiles = User.objects.all()
    context = {
        'profiles': profiles,
        }
    return render(request, 'xpert_users/all_users_db_profiles.html', context)

def all_users_db_projects(request):
    """lists all user projects from the database"""
    projects = Projects.objects.all()
    context = {
        'projects': projects,
        }
    
    
    return render(request, 'xpert_users/all_users_db_projects.html', context)

def all_users_db_services(request):
    """lists all user services from the database"""
    services = Service.objects.all()
    context = {
        'services': services,
        }
    return render(request, 'xpert_users/all_users_db_services.html', context)

def all_users_db_reviews(request):
    """lists all user profiles from the database"""
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
        }
    return render(request, 'xpert_users/all_users_db_reviews.html', context)


# SEARCH 

def service_search(request):
    """implements search functionality in the website"""
    if request.method == "POST":
        services = Service.objects.all()
        form = ServiceSearchForm(request.GET)
        if form.is_valid():
            service_name = form.cleaned_data.get("service_name")
            country = form.cleaned_data.get("country")
            region = form.cleaned_data.get("region")
            town = form.cleaned_data.get("town")
            
            if service_name:
                services = services.filter(service_name__icontains=service_name)
            if country:
                services = services.filter(country__icontains=country)
            if region:
                services = services.filter(region__icontains=region)
            if town:
                services = services.filter(town__icontains=town)
    
        context = {
            "services": services,
            "form": form,
        }
    return render(request, "xpert/search_results.html", context)


# HOME
def home_profiles(request):
    """lists all user profiles from the database"""
    profiles = User.objects.all()
    context = {
        'profiles': profiles,
        }
    return render(request, 'xpert/home.html', context)
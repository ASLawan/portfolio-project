from django.urls import path
from . import views 
from xpert_users import views as xp_views


urlpatterns = [
    path("", views.homepage, name='home'),
    # path("dashboard", views.dashboard, name="dashboard"),
    
    path("register", xp_views.register_user, name="register"),
    path("profile", views.create_profile, name="profile"),
    path("project", views.create_project, name="project"),
    path("service", views.create_service, name="service"),
    path("review", views.create_review, name="review"),

    path("update_user/<int:id>", views.update_user, name="update_user"),
    path("update_profile/<int:id>", views.update_profile, name="update_profile"),
    path("update_project/<int:id>", views.update_project, name="update_project"),
    path("update_service/<int:id>", views.update_service, name="update_service"),
    path("update_review/<int:id>", views.update_review, name="update_review"),

    path("delete_user/<int:id>", views.delete_user, name="delete_user"),
    path("delete_profile/<int:id>", views.delete_profile, name="delete_profile"),
    path("delete_project/<int:id>", views.delete_project, name="delete_project"),
    path("delete_service/<int:id>", views.delete_service, name="delete_service"),
    path("delete_review/<int:id>", views.delete_review, name="delete_review"),

    path("profiles", views.all_profiles, name="profiles"),
    path("projects", views.all_projects, name="projects"),
    path("services", views.all_services, name="services"),
    path("reviews", views.all_reviews, name="reviews"),

     # DASHBOARD
    path("db_services/<int:id>", views.all_user_db_services, name="user_db_services"), # db = dashboard
    path("db_projects/<int:id>", views.all_user_db_projects, name="user_db_projects"),

    # ADMIN DASHBOARD
    path("db_profiles", views.all_users_db_profiles, name="db_profiles"), # db = dashboard
    path("db_projects", views.all_users_db_projects, name="db_projects"),
    path("db_services", views.all_users_db_services, name="db_services"),
    path("db_reviews", views.all_users_db_reviews, name="db_reviews"),


    path("projects/<int:id>", views.all_user_projects, name="user_projects"),
    path("services/<int:id>", views.all_user_services, name="user_services"),
    path("reviews/<int:id>", views.all_user_reviews, name="user_reviews"),
    

    path("profile_detail/<int:id>", views.profile_detail, name="profile_detail"),
    path("project_detail/<int:id>", views.project_detail, name="project_detail"),
    path("service_detail/<int:id>", views.service_detail, name="service_detail"),
    path("review_detail/<int:id>", views.review_detail, name="review_detail"),


    # SEARCH RESULTS
    path('search/', views.service_search, name='service_search'),
]



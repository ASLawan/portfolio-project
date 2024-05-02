from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Projects, Service, Reviews

class TestURLs(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'xpert/home.html')

    def test_register_url(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_project_url(self):
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'xpert_users/all_user_db_projects.html')

    def test_service_url(self):
        response = self.client.get(reverse('service'))
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'xpert_users/all_user_db_services.html')

    def test_review_url(self):
        response = self.client.get(reverse('review'))
        self.assertEqual(response.status_code, 302)
        
    
    def test_profiles_url(self):
        response = self.client.get(reverse('profiles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'xpert/profiles.html')

    def test_projects_url(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'xpert/projects.html')

    def test_services_url(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'xpert/services.html')

    def test_reviews_url(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'xpert/reviews.html')


    # def test_db_profiles_url(self):
    #     response = self.client.get(reverse('db_profiles'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'xpert_users/all_users_profiles.html')

    # def test_db_projects_url(self):
    #     response = self.client.get(reverse('db_projects'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'xpert_users/all_users_projects.html')

    # def test_db_services_url(self):
    #     response = self.client.get(reverse('db_services'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'xpert_users/all_users_services.html')

    # def test_db_reviews_url(self):
    #     response = self.client.get(reverse('db_reviews'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'xpert_users/all_users_reviews.html')



class TestModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='provider1', password='password123')
        self.user2 = User.objects.create_user(username='provider2', password='password456')
        self.service1 = Service.objects.create(provider=self.user1, service_name='Service 1', service_description='Description 1')
        self.project1 = Projects.objects.create(provider=self.user1, project_name='Project 1', project_description='Project Description 1', project_status='Completed')
        self.project2 = Projects.objects.create(provider=self.user2, project_name='Project 2', project_description='Project Description 2', project_status='Ongoing')
        self.review1 = Reviews.objects.create(provider=self.user1, project_name=self.project1, project_rating='5', review='Great service!')
        self.review2 = Reviews.objects.create(provider=self.user2, project_name=self.project2, project_rating='4', review='Good work!')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 2)

    def test_service_creation(self):
        self.assertEqual(Service.objects.count(), 1)
        service = Service.objects.first()
        self.assertEqual(service.provider.username, 'provider1')
        self.assertEqual(service.service_name, 'Service 1')

    def test_project_creation(self):
        self.assertEqual(Projects.objects.count(), 2)
        project = Projects.objects.get(project_name='Project 1')
        self.assertEqual(project.provider.username, 'provider1')
        self.assertEqual(project.project_status, 'Completed')

    def test_review_creation(self):
        self.assertEqual(Reviews.objects.count(), 2)
        review = Reviews.objects.get(review='Great service!')
        self.assertEqual(review.provider.username, 'provider1')
        self.assertEqual(review.project_rating, '5')

    # TEST UPDATE
    def test_update_user_view(self):
        url = reverse('update_user', args=[self.user1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Add more assertions as needed

    def test_update_profile_view(self):
        url = reverse('update_profile', args=[self.user1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Add more assertions as needed

    def test_update_project_view(self):
        url = reverse('update_project', args=[self.project1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Add more assertions as needed

    def test_update_service_view(self):
        url = reverse('update_service', args=[self.service1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # Add more assertions as needed

    def test_update_review_view(self):
        url = reverse('update_review', args=[self.review1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


    # TEST DELETE
    def test_delete_user_view(self):
        url = reverse('delete_user', args=[self.user1.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        # self.assertFalse(User.objects.filter(id=self.user1.id).exists())

    def test_delete_service_view(self):
        url = reverse('delete_service', args=[self.service1.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        # self.assertFalse(Service.objects.filter(id=self.service1.id).exists())

    def test_delete_project_view(self):
        url = reverse('delete_project', args=[self.project1.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        # self.assertFalse(Projects.objects.filter(id=self.project1.id).exists())

    def test_delete_review_view(self):
        url = reverse('delete_review', args=[self.review1.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        # self.assertFalse(Reviews.objects.filter(id=self.review1.id).exists())

    # TEST READ 
    def test_profile_detail_url(self):
        response = self.client.get(reverse('profile_detail', args=[self.user1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'xpert/profile_detail.html')

    def test_project_detail_url(self):
        response = self.client.get(reverse('project_detail', args=[self.project1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'xpert/project_detail.html')

    # def test_service_detail_url(self):
    #     response = self.client.get(reverse('service_detail', args=[self.service1.id]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'xpert/service_detail.html')

    # def test_review_detail_url(self):
    #     response = self.client.get(reverse('review_detail', args=[self.review1.id]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'xpert/review_detail.html')


    def tearDown(self):
        User.objects.all().delete()
        Service.objects.all().delete()
        Projects.objects.all().delete()
        Reviews.objects.all().delete()
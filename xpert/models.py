from django.db import models
from xpert_users.models import User

class Service(models.Model):
    """defines service objects created by service providers"""
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=150, null=False, blank=False)
    service_description = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        """formats string representation"""
        return self.service_name


class Projects(models.Model):
    """defines projects completed by service provider"""
    STATUS = {
        "Completed": "Completed",
        "Ongoing": "Ongoing"
    }
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    project_picture = models.ImageField(default='project.jpg', upload_to='project_pictures')
    project_name = models.CharField(max_length=150, null=False, blank=False)
    project_description = models.CharField(max_length=500, null=False, blank=True)
    project_status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        """formats string representation"""
        return self.project_name

class Reviews(models.Model):
    """defines reviews by service seekers for services rendered"""
    RATE = {
        '1': '1 Star',
        '2': '2 Stars',
        '3': '3 Stars',
        '4': '4 Stars',
        '5': '5 Stars'
    }
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE)
    project_rating = models.CharField(max_length=1, choices=RATE)
    review = models.CharField(max_length=500, null=False, blank=False)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """formats string representation"""
        return self.provider.username
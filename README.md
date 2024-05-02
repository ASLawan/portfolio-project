# Xpert: A Service Marketplace Web Application

Xpert is a web application built with Django that connects service providers with potential clients, service seekers.  
The said web application is a marketplace for service providers and service seekers.  The service seekers will have accounts and profiles where they indicate the services they offer and projects they have completed or have ongoing.  
The service seekers have the option of creating accounts or not but can search for and book services from the platform. They can filter these service by country, region, or town.

## Application Features

### User Accounts (Optional for Service Seekers):
- Users can create accounts as service providers or service seekers.  
- Authentication is managed using Django's built-in authentication system.  
- Custom user models are used to add additional fields like account type (service provider or service seeker).

### Service Provider Profiles:
- Create detailed profiles showcasing: 
    - offered services  
    - experience,   
    - projects (both ongoing and completed).    
- Advertise services with clear descriptions and location information (country, region, town).  

### Service Search and Booking:  
- Search for services by category and location filters (country, region, town).  
- View comprehensive provider profiles with service details and experience.  
- Seamless booking system for registered users

### Dashboard
Users (Service providers) are dotted with a dashboard to facilitate them managing their accounts and carrying our CRUD operations. 


## Technology Stack

### Backend:  
- Django framework for handling server-side logic, user authentication,   
database operations (using ORM), and API integrations.

### Frontend: 
- Bootstrap 5 for responsive UI components, forms, and layout design.  
- HTML   
- CSS  
- JavaScript  

### Database: 

#### Local Development
- SQLite3  

#### Production
- PostgreSQL for data storage, ensuring scalability and reliability.

### Dependencies
- Crispy_forms  
- Pillow  
PS: see more in the requirements.txt file

## Installation

### Clone the repository:
```
git clone https://github.com/ASLawan/portfolio-project.git
```

### Navigate to the project directory:
```
cd portfolio-project
```

### Create a virtual environment:
```
python3 -m venv venv (use any name of your liking)
```

### Activate the virtual environment:

 #### On Linux/macOS:
 ```
 - source venv/bin/activate
 ```

#### On Windows:
```
- venv\Scripts\activate
```

### Install dependencies:
```
pip install -r requirements.txt
```

### Run migrations:
```
- python manage.py migrate
```
### Create a superuser (admin):
```
- python manage.py createsuperuser
```
### Start the development server:
```
- python manage.py runserver
```

## Usage

### Access the admin panel:  
- Navigate to [Django admin panel](http://127.0.0.1:8000/admin)  
- Log in with the superuser credentials created earlier.

### Access the application:
- Navigate to [Application homepage](http://127.0.0.1:8000/)  
- Register as a service provider or service seeker.  
- Create and manage your profile (service providers) or   
- Search and book services (service seekers).
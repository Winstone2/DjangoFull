
from django.urls import path
from NewsApp.views import News, Home, Contact  # Import your actual view function

urlpatterns = [
    path('', Home, name='Home'),
    path('News/', News, name='News'),
    path('Contact/', Contact, name='Contact'),# Add this line for the root path
]
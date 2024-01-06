
from django.urls import path
from NewsApp.views import News  # Import your actual view function

urlpatterns = [
    path('', News, name='News'),  # Add this line for the root path
]
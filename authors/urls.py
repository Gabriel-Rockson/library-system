from django.urls import path
from .views import all_authors

urlpatterns = [path("", all_authors, name="all_authors")]

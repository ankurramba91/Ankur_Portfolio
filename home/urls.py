from django.contrib import admin
from django.urls import path, include
from home import views


#Django Admin Page Customization
admin.site.site_header = "Login to Ankur Portfolio"
admin.site.site_title = "Welcome to DashBoard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]
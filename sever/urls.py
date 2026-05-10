"""
URL configuration for sever project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.base,name='base'),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('error',views.error,name='error'),
    path('appointment',views.appointment,name='appointment'),
    path('contact',views.contact,name='contact'),
    path('courses',views.courses,name='courses'),
    path('feature',views.feature,name='feature'),
    path('team',views.team,name='team'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

handler404 = 'web.views.error'

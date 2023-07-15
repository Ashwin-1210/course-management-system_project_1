"""Skola_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .import views
from .import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('', views.HOME, name='home'),
    path('courses', views.SINGLE_COURSE, name='course'),
    path('course/<slug:slug>', views.COURSE_DETAILS, name='course_details'),
    path('filter-data', views.filter_data, name="filter-data"),
    path('contect', views.CONTECT_US, name='contect'),
    path('about', views.ABOUT_US, name='about'),
    # path('login', user_login.LOGIN, name='login'),
    path('register', user_login.REGISTER, name='register'),
    path('password_reset', views.RESET, name='password_reset'),
    path('search', views.SEARCH_COURSE, name='search_course'),
    path('404', views.PAGE_NOT_FOUND, name='404'),
    path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),
    path('my-course', views.MY_COURSE, name='my_course'),
    #path('course/watch-course/<slug:slug>',views.WATCH_COURSE, name='watch_course'),







    #path('logout', views.LOGOUT, name='logout'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

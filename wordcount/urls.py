"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import view

urlpatterns = [
    #path('admin/', admin.site.urls),
	path('', view.Home, name = "home"),
	path('sham/', view.shamDetails),
	
	
	#path('count/', view.countWords ),
	#	Here if the url path changes  like  count --> counts then we will get error
	#	ie..   on button click in home page through form action it will redirect to count page( as url)the request 	will
	#	be handled in URL -->urlpatterns, checks the. Since there is mismatch in path gives error ......  
	#	SOLUTION --->  Add name parameter
	
	path('count/', view.countWords , name = "CountWords"),
	path('about/', view.gotoAboutPage, name = "about"),
	
]

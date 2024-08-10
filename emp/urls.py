"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from emp import views

urlpatterns = [
    path('home/',views.emp_list,name='home'),
    path('add-emp/',views.add_emp),
    path('delete-emp/<str:eid>',views.delete_emp),
    path('update-emp/<str:eid>',views.update_emp),
    path('testimonial/',views.testimonial),
    path('testimonial/viewtesti/',views.viewtesti),
    path('testimonial/down/<int:pk>/',views.download_file,name='download_file'), 

]

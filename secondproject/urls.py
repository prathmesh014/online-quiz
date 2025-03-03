"""
URL configuration for secondproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from atexit import register
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore

from secondapp.views import   AdminToLogin, adduser, adminlogin, countQNO, dashboard, deleteQbySUB_Qno, deleteUser,   endexam, getQbySUB, getQbySUB_Qno, getUser, getallUser, getallquestions, getonlyPYTHONq,   giveMeRegister, giveMelogin,  addquestion, deletequestion, hello,display, login,  nextQuestion, previousQuestion, sendData, starttest, updateUser,  updatequestion, viewquestion,register, viewresults

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello),
    path('display/',display),
    path('addquestion/',addquestion),
    path('viewquestion/',viewquestion), 
    path('deletequestion/',deletequestion),
    path('updatequestion/',updatequestion),
    path('giveMeRegister/',giveMeRegister),
    path('giveMelogin/',giveMelogin),
    path('register/',register),
    path('login/',login),
    path('nextQuestion/',nextQuestion),
    path('previousQuestion/',previousQuestion),
    path('endexam/',endexam),
    path('starttest/',starttest),
    path('adminlogin/',adminlogin),
    path('AdminToLogin/',AdminToLogin),

    path('sendData/',sendData),
    path('dashboard/',dashboard),
  
    path('viewresults/',viewresults),
    
    
    path('getallUser/',getallUser),
    path('getUser/<username>',getUser),
    path('deleteUser/',deleteUser),
    path('getallquestions/',getallquestions),
    path('getonlyPYTHONq/', getonlyPYTHONq),
    path('getQbySUB/',getQbySUB),
    path('getQbySUB_Qno/',getQbySUB_Qno),
    path('deleteQbySUB_Qno/',deleteQbySUB_Qno),
    path('countQNO/',countQNO),
    path('adduser/',adduser),
    path('updateUser/',updateUser)
]

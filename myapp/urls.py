from django.urls import path
from myapp import views
print('In urls.py in myapp')
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
]

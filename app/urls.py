
from django.urls import path,include
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.meals, name='meal'),
    
    
]
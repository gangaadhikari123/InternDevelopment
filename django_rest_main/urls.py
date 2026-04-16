
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Web application endpoints

    path('students/', include('students.urls')),

    #API ENdpoint
    path('api/v1/',include ('api.urls'))

]

from django.contrib import admin
from django.urls import path, include
from .views import *
from api.views import *
from authentification.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('about', about),
    path('loaded-images', loaded_images),
    path('newimages<int:image_id>/', new_image_view, name='new_image_view'),
    path('images', images),
    
    path('books/', include('api.urls')),
    
    path('accounts/', include('authentification.urls')),
    
    path('', index), # this shit '' should be the last one !!
]

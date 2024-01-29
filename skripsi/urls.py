from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BWM_MARCOS.urls')),
    path('ILP/', include('ILP.urls')),
    path('', include('UserAccount.urls')),
    path('blog/', include('blog.urls')),
]

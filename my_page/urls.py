from django.urls import path, include

urlpatterns = [
    path('', include('page_app.urls')),
]

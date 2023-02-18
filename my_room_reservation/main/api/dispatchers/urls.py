from django.urls import path, include


urlpatterns = [
    path('auth/', include('main.api.dispatchers.registration.register_dispatcher')),
]

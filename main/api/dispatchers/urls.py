from django.urls import path, include


urlpatterns = [
    path('auth/', include('main.api.dispatchers.registration.register_dispatcher')),
    path('room/', include('main.api.dispatchers.room.room_dispatcher')),
    path('seat/', include('main.api.dispatchers.seat.seat_dispatcher')),
    path('reservation/', include('main.api.dispatchers.reservation.reservation_dispatcher')),
    path('resell/', include('main.api.dispatchers.resell.resell_dispatcher')),
    path('notif/', include('main.api.dispatchers.notif.notif_dispatcher')),
    path('comment/', include('main.api.dispatchers.comment.comment_dispatcher'))
]

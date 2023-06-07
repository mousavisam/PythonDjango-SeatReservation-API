from django.db.models import QuerySet

from ...enum.notification_type import NotificationType
from ...model.notification_entity import Notification


class NotificationLogic:

    def insert_notif(self, **kwargs):
        Notification.objects.create(**kwargs)

    def close_notif(self, notif_id: int) -> None:
        notif = Notification.objects.filter(id=notif_id).first()
        notif.is_read = True
        notif.save()

    def get_notif_by_user_id(self, user_id: int) -> QuerySet:
        return Notification.objects.filter(user__id=user_id, is_read=False)

    def get_notif_by_type(self, notif_type: NotificationType) -> QuerySet:
        return Notification.objects.filter(type=notif_type, is_read=False)

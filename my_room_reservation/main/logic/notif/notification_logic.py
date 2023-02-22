from ...model.notification_entity import Notification


class NotificationLogic:

    def insert_notif(self, **kwargs):
        return Notification.objects.create(**kwargs)

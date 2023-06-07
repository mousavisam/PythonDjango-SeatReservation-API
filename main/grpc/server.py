import time

from main.enum.notification_type import NotificationType
from main.grpc.proto.room_reservation_pb2 import NotifRequest, NotifResponse
from main.grpc.proto.room_reservation_pb2_grpc import RoomReservationServicer
from main.logic.notif.notification_logic import NotificationLogic

from main.shared.utils import RoomReservationUtils


class RoomReservationService(RoomReservationServicer):

    def __init__(self, *args, **kwargs):
        self.notif_logic = NotificationLogic()

    def ServeNotification(self, request: NotifRequest, context):
        user_id = request.user_id

        def get_notif(user_id=None):
            if user_id:
                notifs = self.notif_logic.get_notif_by_user_id(user_id)
            else:
                notifs = self.notif_logic.get_notif_by_type(notif_type=NotificationType.PUBLIC)
            return notifs

        while True:

            notifs = get_notif(user_id)
            for notif in notifs:
                response_grpc = NotifResponse()

                response_grpc.message = notif.message
                response_grpc.creation_time = RoomReservationUtils.convert_datetime_to_str(notif.creation_time)

                yield response_grpc
            time.sleep(5)
            continue
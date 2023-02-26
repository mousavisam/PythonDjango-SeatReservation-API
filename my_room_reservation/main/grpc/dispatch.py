from main.grpc.server import RoomReservationService

from main.grpc.proto import room_reservation_pb2_grpc


def add_servicers_to_server(server):
    """
    Add all Servicers to Server
    """
    room_reservation_pb2_grpc.add_RoomReservationServicer_to_server(RoomReservationService(), server)
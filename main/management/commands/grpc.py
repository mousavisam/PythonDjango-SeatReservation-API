from django.core.management import BaseCommand

from main.grpc.manage_grpc import Serve


class Command(BaseCommand):
    help = "run grpc server"

    def handle(self, *args, **options):
        a = Serve()
        a.serve_grpc()
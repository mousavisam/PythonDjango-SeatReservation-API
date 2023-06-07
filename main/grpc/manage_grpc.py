import logging
import multiprocessing
from concurrent import futures

import grpc

from main.grpc.dispatch import add_servicers_to_server

_PROCESS_COUNT = multiprocessing.cpu_count()


class Serve:
    def __init__(self):
        super().__init__()

    def serve_grpc(self, host: str = "[::]:", port: int = 8100):
        GRPC_THREAD_PER_CPU_CORE = 40
        if GRPC_THREAD_PER_CPU_CORE is not None:
            _THREAD_CONCURRENCY = 40
        else:
            _THREAD_CONCURRENCY = _PROCESS_COUNT * GRPC_THREAD_PER_CPU_CORE

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=_THREAD_CONCURRENCY))
        logging.basicConfig(level=logging.INFO)
        add_servicers_to_server(server)

        serve_url = host + str(port)
        print("Starting gRPC Server on :{}".format(serve_url))
        server.add_insecure_port('%s' % serve_url)
        server.start()
        server.wait_for_termination()
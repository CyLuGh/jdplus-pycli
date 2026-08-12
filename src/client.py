import grpc

from src.jdplus.main.ws.v1.toolkit_basic_pb2_grpc import TsFunctionsStub
from src.jdplus.main.ws.v1.toolkit_messages_pb2 import EmptyDto
from src.models import VersionInfo


class CommunicationManager:
    url: str
    def __init__(self):
        self.url = 'localhost:4566'

    def get_version(self) -> VersionInfo:
        with grpc.insecure_channel(self.url) as channel:
            stub = TsFunctionsStub(channel)
            req = EmptyDto()
            dto = stub.GetVersion(req)
            return VersionInfo(dto)


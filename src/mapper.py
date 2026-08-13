from jdplus.main.ws.v1.toolkit_messages_pb2 import VersionInfoDto
from models import VersionInfo


class Mapper:
    @staticmethod
    def to_model(dto: VersionInfoDto) -> VersionInfo:
        VersionInfo(major=dto.major, minor=dto.minor, revision=dto.revision)
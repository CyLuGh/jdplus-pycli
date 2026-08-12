from src.jdplus.main.ws.v1.toolkit_messages_pb2 import VersionInfoDto


class VersionInfo:
    """Service version information"""

    major: int
    minor: int
    revision: int

    def __init__(self, dto: VersionInfoDto):
        self.major = dto.major
        self.minor = dto.minor
        self.revision = dto.revision

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.revision}'


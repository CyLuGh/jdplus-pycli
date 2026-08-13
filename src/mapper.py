from jdplus.main.ws.v1.toolkit_messages_pb2 import VersionInfoDto, TsDataDto, TsPeriodDto, DescriptiveStatisticsDto, \
    DateDto
from models import VersionInfo, TsData, TsPeriod, DescriptiveStatistics, ResultStatus

from datetime import date



class VersionInfoMapper:
    @staticmethod
    def to_model(dto: VersionInfoDto) -> VersionInfo:
        return VersionInfo(major=dto.major, minor=dto.minor, revision=dto.revision)

class TsPeriodMapper:
    @staticmethod
    def to_dto(model: TsPeriod) -> TsPeriodDto:
        dto = TsPeriodDto()
        dto.frequency = model.frequency
        dto.pos = model.position
        dto.year = model.year
        return dto

    @staticmethod
    def to_model(dto: TsPeriodDto) -> TsPeriod:
        return TsPeriod(frequency=dto.frequency, position=dto.pos, year=dto.year)

class TsDataMapper:
    @staticmethod
    def to_dto(model: TsData) -> TsDataDto:
        dto = TsDataDto()
        dto.start.frequency = model.start.frequency
        dto.start.pos = model.start.position
        dto.start.year = model.start.year
        dto.values.extend(model.values)
        return dto

    @staticmethod
    def to_model(dto: TsDataDto) -> TsData:
        start= TsPeriodMapper.to_model(dto.start)
        values= tuple(dto.values)
        return TsData(
            start= start,
            values= values
        )

class DateMapper:
    @staticmethod
    def to_dto(model: date) -> DateDto:
        dto = DateDto()
        dto.year = model.year
        dto.month = model.month
        dto.day = model.day
        return dto

class DescriptiveStatisticsMapper:
    @staticmethod
    def to_model(dto: DescriptiveStatisticsDto) -> DescriptiveStatistics:
        model = DescriptiveStatistics(
            id = dto.id,
            n= dto.n,
            n_missing= dto.nmissing,
            max= dto.max,
            min= dto.min,
            average= dto.average,
            std_dev= dto.stdev,
            q25= dto.q25,
            q50= dto.q50,
            q75= dto.q75,
            status= ResultStatus(type=dto.status.type, message=dto.status.message)
        )
        return model
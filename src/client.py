import grpc

from mapper import VersionInfoMapper, TsDataMapper, DescriptiveStatisticsMapper, DateMapper
from src.jdplus.main.ws.v1.toolkit_basic_pb2_grpc import TsFunctionsStub
from src.jdplus.main.ws.v1.toolkit_messages_pb2 import EmptyDto, TsFunctionInputDto, BuildTsDataInputDto, \
    BuildTsDataObsDto
from src.models import VersionInfo, DescriptiveStatistics, Frequency, TsData, Observation, AggregationType


class CommunicationManager:
    url: str
    def __init__(self):
        self.url = 'localhost:4566'

    def get_version(self) -> VersionInfo:
        with grpc.insecure_channel(self.url) as channel:
            stub = TsFunctionsStub(channel)
            req = EmptyDto()
            dto = stub.GetVersion(req)
            return VersionInfoMapper.to_model(dto)

    def get_descriptive_statistics(self, ts_data: TsData) -> DescriptiveStatistics:
        with grpc.insecure_channel(self.url) as channel:
            stub = TsFunctionsStub(channel)
            req = TsFunctionInputDto(id= "", series= TsDataMapper.to_dto(ts_data))
            dto = stub.Statistics(req)
            return DescriptiveStatisticsMapper.to_model(dto)

    def build_ts_data(self,
                      data: tuple[Observation],
                      aggregation_type: AggregationType = AggregationType.NONE,
                      frequency: Frequency = Frequency.YEARLY,
                      allow_partial_aggregation: bool = True,
                      include_missing_values: bool = True
                      ) -> TsData:
        with grpc.insecure_channel(self.url) as channel:
            stub = TsFunctionsStub(channel)
            req = BuildTsDataInputDto()
            req.gathering.aggregation_type = aggregation_type
            req.gathering.frequency = frequency
            req.gathering.allow_partial_aggregation = allow_partial_aggregation
            req.gathering.include_missing_values = include_missing_values
            req.id = ""
            req.observations.extend([ BuildTsDataObsDto(date=DateMapper.to_dto(observation.date),  value=observation.value) for observation in data ])
            dto = stub.BuildTsData(req)
            return TsDataMapper.to_model(dto.series)


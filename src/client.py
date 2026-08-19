import grpc

from mapper import VersionInfoMapper, TsDataMapper, DescriptiveStatisticsMapper, DateMapper, \
    TemporalDisaggregationResultsMapper
from src.jdplus.main.ws.v1.toolkit_basic_pb2_grpc import TsFunctionsStub
from src.jdplus.main.ws.v1.toolkit_messages_pb2 import EmptyDto, TsFunctionInputDto, BuildTsDataInputDto, \
    BuildTsDataObsDto, TemporalDisaggregationRequestDto
from src.models import VersionInfo, DescriptiveStatistics, Frequency, TsData, Observation, AggregationType, \
    TemporalDisaggregationResults


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

    def process_temporal_disaggregation(self,
                               y: TsData,
                               constant: bool,
                               trend: bool,
                               model: str,
                               freq: int,
                               average: bool,
                               rho: float,
                               fixed_rho: bool,
                               truncated_rho: float,
                               zero_init: bool,
                               algorithm: str,
                               diffuser_egs: bool,
                               n_backcasts: int,
                               n_forecasts: int) -> TemporalDisaggregationResults:
        with grpc.insecure_channel(self.url) as channel:
            stub = TsFunctionsStub(channel)
            req = TemporalDisaggregationRequestDto()
            req.y.start.year = y.start.year
            req.y.start.pos = y.start.position
            req.y.start.frequency = y.start.frequency
            req.y.values.extend(y.values)
            req.constant = constant
            req.trend = trend
            req.model = model
            req.frequency = freq
            req.average = average
            req.rho = rho
            req.fixedRho = fixed_rho
            req.truncatedRho = truncated_rho
            req.zeroInit = zero_init
            req.algorithm = algorithm
            req.diffuserEgs = diffuser_egs
            req.n_backcasts = n_backcasts
            req.n_forecasts = n_forecasts
            dto = stub.ProcessTemporalDisaggregation(req)
            return TemporalDisaggregationResultsMapper.to_model(dto)
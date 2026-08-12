from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Frequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FREQ_UNDEFINED: _ClassVar[Frequency]
    FREQ_YEARLY: _ClassVar[Frequency]
    FREQ_HALF_YEARLY: _ClassVar[Frequency]
    FREQ_QUADRI_MONTHLY: _ClassVar[Frequency]
    FREQ_QUARTERLY: _ClassVar[Frequency]
    FREQ_BI_MONTHLY: _ClassVar[Frequency]
    FREQ_MONTHLY: _ClassVar[Frequency]
    FREQ_DAILY: _ClassVar[Frequency]

class SelectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPAN_ALL: _ClassVar[SelectionType]
    SPAN_FROM: _ClassVar[SelectionType]
    SPAN_TO: _ClassVar[SelectionType]
    SPAN_BETWEEN: _ClassVar[SelectionType]
    SPAN_LAST: _ClassVar[SelectionType]
    SPAN_FIRST: _ClassVar[SelectionType]
    SPAN_EXCLUDING: _ClassVar[SelectionType]
    SPAN_NONE: _ClassVar[SelectionType]

class ResultStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_OK: _ClassVar[ResultStatusType]
    STATUS_ERROR: _ClassVar[ResultStatusType]
    STATUS_WARNING: _ClassVar[ResultStatusType]

class AggregationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGGREGATION_NONE: _ClassVar[AggregationType]
    AGGREGATION_SUM: _ClassVar[AggregationType]
    AGGREGATION_AVERAGE: _ClassVar[AggregationType]
    AGGREGATION_FIRST: _ClassVar[AggregationType]
    AGGREGATION_LAST: _ClassVar[AggregationType]
    AGGREGATION_MAX: _ClassVar[AggregationType]
    AGGREGATION_MIN: _ClassVar[AggregationType]

class DistributionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIST_FIRST: _ClassVar[DistributionType]
    DIST_LAST: _ClassVar[DistributionType]
    DIST_MIDDLE: _ClassVar[DistributionType]

class ValueStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VS_PRESENT: _ClassVar[ValueStatus]
    VS_UNUSED: _ClassVar[ValueStatus]
    VS_BEFORE: _ClassVar[ValueStatus]
    VS_AFTER: _ClassVar[ValueStatus]
    VS_EMPTY: _ClassVar[ValueStatus]

class ParameterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARAMETER_UNUSED: _ClassVar[ParameterType]
    PARAMETER_UNDEFINED: _ClassVar[ParameterType]
    PARAMETER_FIXED: _ClassVar[ParameterType]
    PARAMETER_INITIAL: _ClassVar[ParameterType]
    PARAMETER_ESTIMATED: _ClassVar[ParameterType]
FREQ_UNDEFINED: Frequency
FREQ_YEARLY: Frequency
FREQ_HALF_YEARLY: Frequency
FREQ_QUADRI_MONTHLY: Frequency
FREQ_QUARTERLY: Frequency
FREQ_BI_MONTHLY: Frequency
FREQ_MONTHLY: Frequency
FREQ_DAILY: Frequency
SPAN_ALL: SelectionType
SPAN_FROM: SelectionType
SPAN_TO: SelectionType
SPAN_BETWEEN: SelectionType
SPAN_LAST: SelectionType
SPAN_FIRST: SelectionType
SPAN_EXCLUDING: SelectionType
SPAN_NONE: SelectionType
STATUS_OK: ResultStatusType
STATUS_ERROR: ResultStatusType
STATUS_WARNING: ResultStatusType
AGGREGATION_NONE: AggregationType
AGGREGATION_SUM: AggregationType
AGGREGATION_AVERAGE: AggregationType
AGGREGATION_FIRST: AggregationType
AGGREGATION_LAST: AggregationType
AGGREGATION_MAX: AggregationType
AGGREGATION_MIN: AggregationType
DIST_FIRST: DistributionType
DIST_LAST: DistributionType
DIST_MIDDLE: DistributionType
VS_PRESENT: ValueStatus
VS_UNUSED: ValueStatus
VS_BEFORE: ValueStatus
VS_AFTER: ValueStatus
VS_EMPTY: ValueStatus
PARAMETER_UNUSED: ParameterType
PARAMETER_UNDEFINED: ParameterType
PARAMETER_FIXED: ParameterType
PARAMETER_INITIAL: ParameterType
PARAMETER_ESTIMATED: ParameterType

class EmptyDto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DateDto(_message.Message):
    __slots__ = ("year", "month", "day")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    day: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class TsPeriodDto(_message.Message):
    __slots__ = ("frequency", "year", "pos")
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    frequency: Frequency
    year: int
    pos: int
    def __init__(self, frequency: _Optional[_Union[Frequency, str]] = ..., year: _Optional[int] = ..., pos: _Optional[int] = ...) -> None: ...

class TsDataDto(_message.Message):
    __slots__ = ("start", "values")
    START_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    start: TsPeriodDto
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, start: _Optional[_Union[TsPeriodDto, _Mapping]] = ..., values: _Optional[_Iterable[float]] = ...) -> None: ...

class MatrixDto(_message.Message):
    __slots__ = ("nrows", "ncols", "values")
    NROWS_FIELD_NUMBER: _ClassVar[int]
    NCOLS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    nrows: int
    ncols: int
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, nrows: _Optional[int] = ..., ncols: _Optional[int] = ..., values: _Optional[_Iterable[float]] = ...) -> None: ...

class TsMatrixDto(_message.Message):
    __slots__ = ("start", "values")
    START_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    start: TsPeriodDto
    values: MatrixDto
    def __init__(self, start: _Optional[_Union[TsPeriodDto, _Mapping]] = ..., values: _Optional[_Union[MatrixDto, _Mapping]] = ...) -> None: ...

class TsMonikerDto(_message.Message):
    __slots__ = ("source", "id")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    source: str
    id: str
    def __init__(self, source: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class TsDto(_message.Message):
    __slots__ = ("name", "moniker", "data", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MONIKER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    moniker: TsMonikerDto
    data: TsDataDto
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., moniker: _Optional[_Union[TsMonikerDto, _Mapping]] = ..., data: _Optional[_Union[TsDataDto, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TsObservationDto(_message.Message):
    __slots__ = ("start", "end", "value")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    start: DateDto
    end: DateDto
    value: float
    def __init__(self, start: _Optional[_Union[DateDto, _Mapping]] = ..., end: _Optional[_Union[DateDto, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class TimeSeriesDto(_message.Message):
    __slots__ = ("name", "moniker", "observations", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MONIKER_FIELD_NUMBER: _ClassVar[int]
    OBSERVATIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    moniker: TsMonikerDto
    observations: _containers.RepeatedCompositeFieldContainer[TsObservationDto]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., moniker: _Optional[_Union[TsMonikerDto, _Mapping]] = ..., observations: _Optional[_Iterable[_Union[TsObservationDto, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TimeSelectorDto(_message.Message):
    __slots__ = ("type", "n0", "n1", "d0", "d1")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    N0_FIELD_NUMBER: _ClassVar[int]
    N1_FIELD_NUMBER: _ClassVar[int]
    D0_FIELD_NUMBER: _ClassVar[int]
    D1_FIELD_NUMBER: _ClassVar[int]
    type: SelectionType
    n0: int
    n1: int
    d0: DateDto
    d1: DateDto
    def __init__(self, type: _Optional[_Union[SelectionType, str]] = ..., n0: _Optional[int] = ..., n1: _Optional[int] = ..., d0: _Optional[_Union[DateDto, _Mapping]] = ..., d1: _Optional[_Union[DateDto, _Mapping]] = ...) -> None: ...

class ResultStatusDto(_message.Message):
    __slots__ = ("type", "message")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: ResultStatusType
    message: str
    def __init__(self, type: _Optional[_Union[ResultStatusType, str]] = ..., message: _Optional[str] = ...) -> None: ...

class TsFunctionInputDto(_message.Message):
    __slots__ = ("id", "series")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    series: TsDataDto
    def __init__(self, id: _Optional[str] = ..., series: _Optional[_Union[TsDataDto, _Mapping]] = ...) -> None: ...

class TsFunctionOutputDto(_message.Message):
    __slots__ = ("id", "status", "series")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: ResultStatusDto
    series: TsDataDto
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[ResultStatusDto, _Mapping]] = ..., series: _Optional[_Union[TsDataDto, _Mapping]] = ...) -> None: ...

class PctInputDto(_message.Message):
    __slots__ = ("id", "series", "lag")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    LAG_FIELD_NUMBER: _ClassVar[int]
    id: str
    series: TsDataDto
    lag: int
    def __init__(self, id: _Optional[str] = ..., series: _Optional[_Union[TsDataDto, _Mapping]] = ..., lag: _Optional[int] = ...) -> None: ...

class DeltaInputDto(_message.Message):
    __slots__ = ("id", "series", "lag", "power")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    LAG_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    id: str
    series: TsDataDto
    lag: int
    power: int
    def __init__(self, id: _Optional[str] = ..., series: _Optional[_Union[TsDataDto, _Mapping]] = ..., lag: _Optional[int] = ..., power: _Optional[int] = ...) -> None: ...

class AggregationInputDto(_message.Message):
    __slots__ = ("id", "series", "aggregation_type", "new_frequency", "complete")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEW_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    id: str
    series: TsDataDto
    aggregation_type: AggregationType
    new_frequency: Frequency
    complete: bool
    def __init__(self, id: _Optional[str] = ..., series: _Optional[_Union[TsDataDto, _Mapping]] = ..., aggregation_type: _Optional[_Union[AggregationType, str]] = ..., new_frequency: _Optional[_Union[Frequency, str]] = ..., complete: _Optional[bool] = ...) -> None: ...

class HodrickPrescottInputDto(_message.Message):
    __slots__ = ("id", "series")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    LAMBDA_FIELD_NUMBER: _ClassVar[int]
    id: str
    series: TsDataDto
    def __init__(self, id: _Optional[str] = ..., series: _Optional[_Union[TsDataDto, _Mapping]] = ..., **kwargs) -> None: ...

class HodrickPrescottOutputDto(_message.Message):
    __slots__ = ("id", "status", "trend", "noise")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TREND_FIELD_NUMBER: _ClassVar[int]
    NOISE_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: ResultStatusDto
    trend: TsDataDto
    noise: TsDataDto
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[ResultStatusDto, _Mapping]] = ..., trend: _Optional[_Union[TsDataDto, _Mapping]] = ..., noise: _Optional[_Union[TsDataDto, _Mapping]] = ...) -> None: ...

class DescriptiveStatisticsDto(_message.Message):
    __slots__ = ("id", "status", "n", "nmissing", "max", "min", "average", "stdev", "q25", "q50", "q75")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    NMISSING_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_FIELD_NUMBER: _ClassVar[int]
    STDEV_FIELD_NUMBER: _ClassVar[int]
    Q25_FIELD_NUMBER: _ClassVar[int]
    Q50_FIELD_NUMBER: _ClassVar[int]
    Q75_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: ResultStatusDto
    n: int
    nmissing: int
    max: float
    min: float
    average: float
    stdev: float
    q25: float
    q50: float
    q75: float
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[ResultStatusDto, _Mapping]] = ..., n: _Optional[int] = ..., nmissing: _Optional[int] = ..., max: _Optional[float] = ..., min: _Optional[float] = ..., average: _Optional[float] = ..., stdev: _Optional[float] = ..., q25: _Optional[float] = ..., q50: _Optional[float] = ..., q75: _Optional[float] = ...) -> None: ...

class ObsGatheringDto(_message.Message):
    __slots__ = ("frequency", "aggregation_type", "allow_partial_aggregation", "include_missing_values")
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PARTIAL_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MISSING_VALUES_FIELD_NUMBER: _ClassVar[int]
    frequency: Frequency
    aggregation_type: AggregationType
    allow_partial_aggregation: bool
    include_missing_values: bool
    def __init__(self, frequency: _Optional[_Union[Frequency, str]] = ..., aggregation_type: _Optional[_Union[AggregationType, str]] = ..., allow_partial_aggregation: _Optional[bool] = ..., include_missing_values: _Optional[bool] = ...) -> None: ...

class BuildTsDataObsDto(_message.Message):
    __slots__ = ("date", "value")
    DATE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    date: DateDto
    value: float
    def __init__(self, date: _Optional[_Union[DateDto, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class BuildTsDataInputDto(_message.Message):
    __slots__ = ("id", "gathering", "observations")
    ID_FIELD_NUMBER: _ClassVar[int]
    GATHERING_FIELD_NUMBER: _ClassVar[int]
    OBSERVATIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    gathering: ObsGatheringDto
    observations: _containers.RepeatedCompositeFieldContainer[BuildTsDataObsDto]
    def __init__(self, id: _Optional[str] = ..., gathering: _Optional[_Union[ObsGatheringDto, _Mapping]] = ..., observations: _Optional[_Iterable[_Union[BuildTsDataObsDto, _Mapping]]] = ...) -> None: ...

class BuildTsDataTableInputDto(_message.Message):
    __slots__ = ("id", "distribution_type", "collection")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    distribution_type: DistributionType
    collection: _containers.RepeatedCompositeFieldContainer[TsDataDto]
    def __init__(self, id: _Optional[str] = ..., distribution_type: _Optional[_Union[DistributionType, str]] = ..., collection: _Optional[_Iterable[_Union[TsDataDto, _Mapping]]] = ...) -> None: ...

class BuildTsDataTableOutputDto(_message.Message):
    __slots__ = ("id", "matrix", "statuses")
    ID_FIELD_NUMBER: _ClassVar[int]
    MATRIX_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    id: str
    matrix: TsMatrixDto
    statuses: _containers.RepeatedScalarFieldContainer[ValueStatus]
    def __init__(self, id: _Optional[str] = ..., matrix: _Optional[_Union[TsMatrixDto, _Mapping]] = ..., statuses: _Optional[_Iterable[_Union[ValueStatus, str]]] = ...) -> None: ...

class TemporalDisaggregationResultsDto(_message.Message):
    __slots__ = ("originalSeries", "disaggregationDomain", "indicators", "hyperParametersCount", "likelihood", "stats", "maximum", "residualsDiagnostics", "disaggregatedSeries", "stDevDisaggregatedSeries", "regressionEffects")
    ORIGINALSERIES_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATIONDOMAIN_FIELD_NUMBER: _ClassVar[int]
    INDICATORS_FIELD_NUMBER: _ClassVar[int]
    HYPERPARAMETERSCOUNT_FIELD_NUMBER: _ClassVar[int]
    LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    RESIDUALSDIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATEDSERIES_FIELD_NUMBER: _ClassVar[int]
    STDEVDISAGGREGATEDSERIES_FIELD_NUMBER: _ClassVar[int]
    REGRESSIONEFFECTS_FIELD_NUMBER: _ClassVar[int]
    originalSeries: TsDataDto
    disaggregationDomain: TsDomainDto
    indicators: _containers.RepeatedCompositeFieldContainer[TsVariableDto]
    hyperParametersCount: int
    likelihood: DiffuseConcentratedLikelihoodDto
    stats: DiffuseLikelihoodStatisticsDto
    maximum: ObjectiveFunctionPointDto
    residualsDiagnostics: ResidualsDiagnosticsDto
    disaggregatedSeries: TsDataDto
    stDevDisaggregatedSeries: TsDataDto
    regressionEffects: TsDataDto
    def __init__(self, originalSeries: _Optional[_Union[TsDataDto, _Mapping]] = ..., disaggregationDomain: _Optional[_Union[TsDomainDto, _Mapping]] = ..., indicators: _Optional[_Iterable[_Union[TsVariableDto, _Mapping]]] = ..., hyperParametersCount: _Optional[int] = ..., likelihood: _Optional[_Union[DiffuseConcentratedLikelihoodDto, _Mapping]] = ..., stats: _Optional[_Union[DiffuseLikelihoodStatisticsDto, _Mapping]] = ..., maximum: _Optional[_Union[ObjectiveFunctionPointDto, _Mapping]] = ..., residualsDiagnostics: _Optional[_Union[ResidualsDiagnosticsDto, _Mapping]] = ..., disaggregatedSeries: _Optional[_Union[TsDataDto, _Mapping]] = ..., stDevDisaggregatedSeries: _Optional[_Union[TsDataDto, _Mapping]] = ..., regressionEffects: _Optional[_Union[TsDataDto, _Mapping]] = ...) -> None: ...

class DiffuseConcentratedLikelihoodDto(_message.Message):
    __slots__ = ("ll", "ssqerr", "ldet", "lddet", "nobs", "nd", "nxd", "res", "b", "bvar", "legacy", "scalingFactor")
    LL_FIELD_NUMBER: _ClassVar[int]
    SSQERR_FIELD_NUMBER: _ClassVar[int]
    LDET_FIELD_NUMBER: _ClassVar[int]
    LDDET_FIELD_NUMBER: _ClassVar[int]
    NOBS_FIELD_NUMBER: _ClassVar[int]
    ND_FIELD_NUMBER: _ClassVar[int]
    NXD_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    BVAR_FIELD_NUMBER: _ClassVar[int]
    LEGACY_FIELD_NUMBER: _ClassVar[int]
    SCALINGFACTOR_FIELD_NUMBER: _ClassVar[int]
    ll: float
    ssqerr: float
    ldet: float
    lddet: float
    nobs: int
    nd: int
    nxd: int
    res: _containers.RepeatedScalarFieldContainer[float]
    b: _containers.RepeatedScalarFieldContainer[float]
    bvar: MatrixDto
    legacy: bool
    scalingFactor: bool
    def __init__(self, ll: _Optional[float] = ..., ssqerr: _Optional[float] = ..., ldet: _Optional[float] = ..., lddet: _Optional[float] = ..., nobs: _Optional[int] = ..., nd: _Optional[int] = ..., nxd: _Optional[int] = ..., res: _Optional[_Iterable[float]] = ..., b: _Optional[_Iterable[float]] = ..., bvar: _Optional[_Union[MatrixDto, _Mapping]] = ..., legacy: _Optional[bool] = ..., scalingFactor: _Optional[bool] = ...) -> None: ...

class TsVariableDto(_message.Message):
    __slots__ = ("name", "id", "lag", "coefficient", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAG_FIELD_NUMBER: _ClassVar[int]
    COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    lag: int
    coefficient: ParameterDto
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., lag: _Optional[int] = ..., coefficient: _Optional[_Union[ParameterDto, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ParameterDto(_message.Message):
    __slots__ = ("value", "type", "description")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    value: float
    type: ParameterType
    description: str
    def __init__(self, value: _Optional[float] = ..., type: _Optional[_Union[ParameterType, str]] = ..., description: _Optional[str] = ...) -> None: ...

class DiffuseLikelihoodStatisticsDto(_message.Message):
    __slots__ = ("nobs", "ndiffuse", "nparams", "degrees_of_freedom", "log_likelihood", "adjusted_log_likelihood", "aic", "aicc", "bic", "ssq", "ssqerr", "ldet", "dcorrection")
    NOBS_FIELD_NUMBER: _ClassVar[int]
    NDIFFUSE_FIELD_NUMBER: _ClassVar[int]
    NPARAMS_FIELD_NUMBER: _ClassVar[int]
    DEGREES_OF_FREEDOM_FIELD_NUMBER: _ClassVar[int]
    LOG_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    ADJUSTED_LOG_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    AIC_FIELD_NUMBER: _ClassVar[int]
    AICC_FIELD_NUMBER: _ClassVar[int]
    BIC_FIELD_NUMBER: _ClassVar[int]
    SSQ_FIELD_NUMBER: _ClassVar[int]
    SSQERR_FIELD_NUMBER: _ClassVar[int]
    LDET_FIELD_NUMBER: _ClassVar[int]
    DCORRECTION_FIELD_NUMBER: _ClassVar[int]
    nobs: int
    ndiffuse: int
    nparams: int
    degrees_of_freedom: int
    log_likelihood: float
    adjusted_log_likelihood: float
    aic: float
    aicc: float
    bic: float
    ssq: float
    ssqerr: float
    ldet: float
    dcorrection: float
    def __init__(self, nobs: _Optional[int] = ..., ndiffuse: _Optional[int] = ..., nparams: _Optional[int] = ..., degrees_of_freedom: _Optional[int] = ..., log_likelihood: _Optional[float] = ..., adjusted_log_likelihood: _Optional[float] = ..., aic: _Optional[float] = ..., aicc: _Optional[float] = ..., bic: _Optional[float] = ..., ssq: _Optional[float] = ..., ssqerr: _Optional[float] = ..., ldet: _Optional[float] = ..., dcorrection: _Optional[float] = ...) -> None: ...

class TsDomainDto(_message.Message):
    __slots__ = ("startPeriod", "length")
    STARTPERIOD_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    startPeriod: TsPeriodDto
    length: int
    def __init__(self, startPeriod: _Optional[_Union[TsPeriodDto, _Mapping]] = ..., length: _Optional[int] = ...) -> None: ...

class ObjectiveFunctionPointDto(_message.Message):
    __slots__ = ("value", "parameters", "gradient", "hessian")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    GRADIENT_FIELD_NUMBER: _ClassVar[int]
    HESSIAN_FIELD_NUMBER: _ClassVar[int]
    value: float
    parameters: _containers.RepeatedScalarFieldContainer[float]
    gradient: _containers.RepeatedScalarFieldContainer[float]
    hessian: MatrixDto
    def __init__(self, value: _Optional[float] = ..., parameters: _Optional[_Iterable[float]] = ..., gradient: _Optional[_Iterable[float]] = ..., hessian: _Optional[_Union[MatrixDto, _Mapping]] = ...) -> None: ...

class ResidualsDiagnosticsDto(_message.Message):
    __slots__ = ("fullResiduals", "niid")
    FULLRESIDUALS_FIELD_NUMBER: _ClassVar[int]
    NIID_FIELD_NUMBER: _ClassVar[int]
    fullResiduals: TsDataDto
    niid: NiidTestsDto
    def __init__(self, fullResiduals: _Optional[_Union[TsDataDto, _Mapping]] = ..., niid: _Optional[_Union[NiidTestsDto, _Mapping]] = ...) -> None: ...

class NiidTestsDto(_message.Message):
    __slots__ = ("mean", "skewness", "kurtosis", "doornik_hansen", "ljung_box", "box_pierce", "seasonal_ljung_box", "seasonal_box_pierce", "runs_number", "runs_length", "up_down_runs_number", "up_down_runs_length", "ljung_box_on_squares", "box_pierce_on_squares")
    MEAN_FIELD_NUMBER: _ClassVar[int]
    SKEWNESS_FIELD_NUMBER: _ClassVar[int]
    KURTOSIS_FIELD_NUMBER: _ClassVar[int]
    DOORNIK_HANSEN_FIELD_NUMBER: _ClassVar[int]
    LJUNG_BOX_FIELD_NUMBER: _ClassVar[int]
    BOX_PIERCE_FIELD_NUMBER: _ClassVar[int]
    SEASONAL_LJUNG_BOX_FIELD_NUMBER: _ClassVar[int]
    SEASONAL_BOX_PIERCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    RUNS_LENGTH_FIELD_NUMBER: _ClassVar[int]
    UP_DOWN_RUNS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UP_DOWN_RUNS_LENGTH_FIELD_NUMBER: _ClassVar[int]
    LJUNG_BOX_ON_SQUARES_FIELD_NUMBER: _ClassVar[int]
    BOX_PIERCE_ON_SQUARES_FIELD_NUMBER: _ClassVar[int]
    mean: StatisticalTestDto
    skewness: StatisticalTestDto
    kurtosis: StatisticalTestDto
    doornik_hansen: StatisticalTestDto
    ljung_box: StatisticalTestDto
    box_pierce: StatisticalTestDto
    seasonal_ljung_box: StatisticalTestDto
    seasonal_box_pierce: StatisticalTestDto
    runs_number: StatisticalTestDto
    runs_length: StatisticalTestDto
    up_down_runs_number: StatisticalTestDto
    up_down_runs_length: StatisticalTestDto
    ljung_box_on_squares: StatisticalTestDto
    box_pierce_on_squares: StatisticalTestDto
    def __init__(self, mean: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., skewness: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., kurtosis: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., doornik_hansen: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., ljung_box: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., box_pierce: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., seasonal_ljung_box: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., seasonal_box_pierce: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., runs_number: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., runs_length: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., up_down_runs_number: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., up_down_runs_length: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., ljung_box_on_squares: _Optional[_Union[StatisticalTestDto, _Mapping]] = ..., box_pierce_on_squares: _Optional[_Union[StatisticalTestDto, _Mapping]] = ...) -> None: ...

class StatisticalTestDto(_message.Message):
    __slots__ = ("value", "pValue", "description")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PVALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    value: float
    pValue: float
    description: str
    def __init__(self, value: _Optional[float] = ..., pValue: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...

class TemporalDisaggregationRequestDto(_message.Message):
    __slots__ = ("y", "constant", "trend", "indicators", "model", "average", "rho", "fixedRho", "truncatedRho", "zeroInit", "algorithm", "diffuserEgs")
    Y_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_FIELD_NUMBER: _ClassVar[int]
    TREND_FIELD_NUMBER: _ClassVar[int]
    INDICATORS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_FIELD_NUMBER: _ClassVar[int]
    RHO_FIELD_NUMBER: _ClassVar[int]
    FIXEDRHO_FIELD_NUMBER: _ClassVar[int]
    TRUNCATEDRHO_FIELD_NUMBER: _ClassVar[int]
    ZEROINIT_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    DIFFUSEREGS_FIELD_NUMBER: _ClassVar[int]
    y: TsDataDto
    constant: bool
    trend: bool
    indicators: _containers.RepeatedCompositeFieldContainer[TsDataDto]
    model: str
    average: bool
    rho: float
    fixedRho: bool
    truncatedRho: float
    zeroInit: bool
    algorithm: str
    diffuserEgs: bool
    def __init__(self, y: _Optional[_Union[TsDataDto, _Mapping]] = ..., constant: _Optional[bool] = ..., trend: _Optional[bool] = ..., indicators: _Optional[_Iterable[_Union[TsDataDto, _Mapping]]] = ..., model: _Optional[str] = ..., average: _Optional[bool] = ..., rho: _Optional[float] = ..., fixedRho: _Optional[bool] = ..., truncatedRho: _Optional[float] = ..., zeroInit: _Optional[bool] = ..., algorithm: _Optional[str] = ..., diffuserEgs: _Optional[bool] = ...) -> None: ...

class VersionInfoDto(_message.Message):
    __slots__ = ("major", "minor", "revision")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    revision: int
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., revision: _Optional[int] = ...) -> None: ...

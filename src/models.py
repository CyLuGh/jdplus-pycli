from dataclasses import dataclass, field
from datetime import date

import pandas as pd
from dateutil.relativedelta import relativedelta
from enum import IntEnum
from pydantic import BaseModel

class AggregationType(IntEnum):
    NONE = 0
    SUM = 1
    AVERAGE = 2
    FIRST = 3
    LAST = 4
    MAX = 5
    MIN = 6

class Frequency(IntEnum):
    UNDEFINED = 0
    """Undefined frequency. To be used when the frequency of an event is unknown."""
    YEARLY = 1
    """One event by year."""
    HALF_YEARLY = 2
    """One event every half-year."""
    QUADRI_MONTHLY = 3
    """One event every four months."""
    QUARTERLY = 4
    """One event every quarter."""
    BI_MONTHLY = 6
    """One event every two months."""
    MONTHLY = 12
    """One event every month."""

class ResultStatusType(IntEnum):
    STATUS_OK = 0
    STATUS_ERROR = 1
    STATUS_WARNING = 2

@dataclass(frozen=True)
class ResultStatus(BaseModel):
    type: ResultStatusType
    message: str

@dataclass(frozen=True)
class DescriptiveStatistics(BaseModel):
    id: str
    status: ResultStatus
    n: int
    n_missing: int
    max: float
    min: float
    average: float
    std_dev: float
    q25: float
    q50: float
    q75: float

    def __str__(self):
        return (
            f"{'N':<15}{self.n}\n"
            f"{'N Missing':<15}{self.n_missing}\n"
            f"{'Max':<15}{self.max}\n"
            f"{'Min':<15}{self.min}\n"
            f"{'Average':<15}{self.average}\n"
            f"{'StDev':<15}{self.std_dev}\n"
            f"{'Q25':<15}{self.q25}\n"
            f"{'Q50':<15}{self.q50}\n"
            f"{'Q75':<15}{self.q75}"
        )

@dataclass(frozen=True)
class Matrix(BaseModel):
    n_rows: int
    n_cols: int
    values: tuple[float]
    """The number of values should be n_rows*n_cols. Values are organized by columns (1st column, 2nd column...)"""

    def __post_init__(self):
        expected = self.n_rows * self.n_cols
        if len(self.values) != expected:
            raise ValueError(f"Expected {expected} values, got {len(self.values)}")

@dataclass(frozen=True)
class TsMoniker(BaseModel):
    source: str
    id: str

    @classmethod
    def default(cls) -> "TsMoniker":
        return cls(id='Default', source='Default')

@dataclass(frozen=True)
class TsObservation(BaseModel):
    start: date
    end: date
    value: float

    @classmethod
    def point(cls, observation_date: date, value: float) -> "TsObservation":
        return cls(start=observation_date, end=observation_date, value=value)

@dataclass(frozen=True)
class TsPeriod(BaseModel):
    frequency: Frequency
    year: int
    position: int
    """Position in the year (from 0 to Frequency excluded)."""

    @classmethod
    def default(cls) -> "TsPeriod":
        return cls(frequency=Frequency.UNDEFINED, year=1900, position=0)

    def to_date(self) -> date:
        return date(self.year, 1,1) + relativedelta(months=self.monthly_occurrences_per_year()*self.position)

    def monthly_occurrences_per_year(self) -> int:
        if self.frequency == Frequency.UNDEFINED:
            return 0
        else:
            return 12 // self.frequency

@dataclass(frozen=True)
class TsData(BaseModel):
    start: TsPeriod
    values: tuple[float,...] = field(default_factory=tuple)

    @classmethod
    def default(cls) -> "TsData":
        return cls(start=TsPeriod.default(), values=())

    def get_date_values(self) -> dict[date,float]:
        start = self.start.to_date()
        occurrences_per_year = self.start.monthly_occurrences_per_year()
        return {start + relativedelta(months=i * occurrences_per_year): value for i, value in enumerate(self.values)}

    def as_dataframe(self) -> pd.DataFrame:
        df = pd.DataFrame({
            "values": self.get_date_values()
        })
        df = df.sort_index()
        return df

@dataclass(frozen=True)
class Ts(BaseModel):
    name: str
    moniker: TsMoniker
    data: TsData
    metadata: dict[str, str] = field(default_factory=dict)

    @classmethod
    def default(cls) -> "Ts":
        return cls(name="Default",data=TsData.default(),moniker=TsMoniker.default())

@dataclass(frozen=True)
class TimeSeries(BaseModel):
    name: str
    moniker: TsMoniker
    data: tuple[TsObservation]
    metadata: dict[str, str] = field(default_factory=dict)

@dataclass(frozen=True)
class VersionInfo(BaseModel):
    """Service version information"""

    major: int
    minor: int
    revision: int

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.revision}'

@dataclass(frozen=True)
class Observation(BaseModel):
    date: date
    value: float

@dataclass(frozen=True)
class DiffuseLikelihoodStatistics(BaseModel):
    n_obs: int
    n_diffuse: int
    n_params: int
    degrees_of_freedom: int
    log_likelihood: float
    adjusted_log_likelihood: float
    aic: float
    aicc: float
    bic: float
    ssq: float
    ldet: float
    dcorrection: float

    def __str__(self):
        return (
            f"{'N Obs':<25}{self.n_obs}\n"
            f"{'N Diffuse':<25}{self.n_diffuse}\n"
            f"{'N Params':<25}{self.n_params}\n"
            f"{'Degrees of freedom':<25}{self.degrees_of_freedom}\n"
            f"{'Log likelihood':<25}{self.log_likelihood}\n"
            f"{'Adjusted log likelihood':<25}{self.adjusted_log_likelihood}\n"
            f"{'AIC':<25}{self.aic}\n"
            f"{'AICC':<25}{self.aicc}\n"
            f"{'BIC':<25}{self.bic}\n"
            f"{'SSQ':<25}{self.ssq}\n"
            f"{'LDet':<25}{self.ldet}\n"
            f"{'DCorrection':<25}{self.dcorrection}"
        )

@dataclass(frozen=True)
class DiffuseConcentratedLikelihood(BaseModel):
    ll: float
    ssqerr: float
    ldet: float
    lddet: float
    n_obs: int
    nd: int
    nxd: int
    bvar: Matrix
    legacy: bool
    scaling_factor: bool
    res: tuple[float, ...] = field(default_factory=tuple)
    b: tuple[float, ...] = field(default_factory=tuple)

    def __str__(self):
        return (
            f"{'N Obs':<25}{self.n_obs}\n"
            f"{'ll':<25}{self.ll}\n"
            f"{'ssqerr':<25}{self.ssqerr}\n"
            f"{'ldet':<25}{self.ldet}\n"
            f"{'lddet':<25}{self.lddet}\n"
            f"{'nd':<25}{self.nd}\n"
            f"{'nxd':<25}{self.nxd}\n"
            f"{'bvar':<25}{self.bvar}\n"
            f"{'legacy':<25}{self.legacy}\n"
            f"{'Scaling factor':<25}{self.scaling_factor}\n"
            f"{'res':<25}{self.res}\n"
            f"{'b':<25}{self.b}\n"
        )

@dataclass(frozen=True)
class TemporalDisaggregationResults(BaseModel):
    """
    Results of temporal disaggregation
    """
    originalSeries: TsData
    disaggregatedSeries: TsData
    stDevDisaggregatedSeries: TsData
    regressionEffects: TsData
    statistics: DiffuseLikelihoodStatistics
    likelihood: DiffuseConcentratedLikelihood

    def as_dataframe(self) -> pd.DataFrame:
        """
        Returns a dataframe containing original and disaggregated series with the standard deviations series as well.
        It may include regression effects if available.
        """
        df = pd.DataFrame({
            "original": self.originalSeries.get_date_values(),
            "disaggregated": self.disaggregatedSeries.get_date_values(),
            "stDevDisaggregated": self.stDevDisaggregatedSeries.get_date_values(),
            "regressionEffects": self.regressionEffects.get_date_values(),
        })
        df = df.sort_index()
        return df

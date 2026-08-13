from dataclasses import dataclass, field
from datetime import date
from dateutil.relativedelta import relativedelta
from enum import Enum,IntEnum

class AggregationType(Enum):
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

class ResultStatusType(Enum):
    STATUS_OK = 0
    STATUS_ERROR = 1
    STATUS_WARNING = 2

@dataclass(frozen=True)
class ResultStatus:
    type: ResultStatusType
    message: str

@dataclass(frozen=True)
class DescriptiveStatistics:
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

@dataclass(frozen=True)
class Matrix:
    n_rows: int
    n_cols: int
    values: tuple[float]
    """The number of values should be n_rows*n_cols. Values are organized by columns (1st column, 2nd column...)"""

    def __post_init__(self):
        expected = self.n_rows * self.n_cols
        if len(self.values) != expected:
            raise ValueError(f"Expected {expected} values, got {len(self.values)}")

@dataclass(frozen=True)
class TsMoniker:
    source: str
    id: str

    @classmethod
    def default(cls) -> "TsMoniker":
        return cls(id='Default', source='Default')

@dataclass(frozen=True)
class TsObservation:
    start: date
    end: date
    value: float

    @classmethod
    def point(cls, observation_date: date, value: float) -> "TsObservation":
        return cls(start=observation_date, end=observation_date, value=value)

@dataclass(frozen=True)
class TsPeriod:
    frequency: Frequency
    year: int
    position: int
    """Position in the year (from 0 to Frequency excluded)."""

    @classmethod
    def default(cls) -> "TsPeriod":
        return cls(frequency=Frequency.UNDEFINED, year=1900, position=0)

    def to_date(self) -> date:
        return date(self.year, 1,1) + relativedelta(months=self.monthly_occurrences_per_year())

    def monthly_occurrences_per_year(self) -> int:
        if self.frequency == Frequency.UNDEFINED:
            return 0
        else:
            return 12 // self.frequency

@dataclass(frozen=True)
class TsData:
    start: TsPeriod
    values: tuple[float] = field(default_factory=tuple)

    @classmethod
    def default(cls) -> "TsData":
        return cls(start=TsPeriod.default())

@dataclass(frozen=True)
class Ts:
    name: str
    moniker: TsMoniker
    data: TsData
    metadata: dict[str, str] = field(default_factory=dict)

    @classmethod
    def default(cls) -> "Ts":
        return cls(name="Default",data=TsData.default(),moniker=TsMoniker.default())

@dataclass(frozen=True)
class TimeSeries:
    name: str
    moniker: TsMoniker
    data: tuple[TsObservation]
    metadata: dict[str, str] = field(default_factory=dict)

@dataclass(frozen=True)
class VersionInfo:
    """Service version information"""

    major: int
    minor: int
    revision: int

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.revision}'


import random
import uuid

from src.models import Frequency, TsData, TsPeriod, Ts, TsMoniker

def generate_ts(year: int = 2000,
                     position: int = 0,
                     frequency: Frequency = Frequency.YEARLY,
                     count: int = 10) -> Ts:
    return Ts(
        name=f"{year}-{position}-{frequency.name}-{count}",
        moniker= TsMoniker(source="Test", id=str(uuid.uuid4())),
        data=generate_ts_data(year=year, position=position, frequency=frequency, count=count)
    )

def generate_ts_data(year: int = 2000,
                     position: int = 0,
                     frequency: Frequency = Frequency.YEARLY,
                     count: int = 10) -> TsData:
    return TsData(
        start=TsPeriod(year=year, position=position, frequency=frequency),
        values=tuple(random.random() * 1000 for _ in range(count))
    )

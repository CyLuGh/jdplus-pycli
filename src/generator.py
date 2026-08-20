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
                     count: int = 10,
                     tweak: bool = False) -> TsData:
    def tweak_random(apply: bool, index: int) -> float:
        if apply:
            remain = index % 6
            match remain:
                case 5: return random.randrange(1100, 1300)
                case 4: return random.randrange(700, 1000)
                case 3: return random.randrange(600, 900)
                case 2: return random.randrange(1200, 1500)
                case _: return random.randrange(950, 1050)
        else:
            return 1000

    return TsData(
        start=TsPeriod(year=year, position=position, frequency=frequency),
        values=tuple(random.random() * tweak_random(tweak,idx) for idx in range(count))
    )

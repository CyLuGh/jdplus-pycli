from generator import generate_ts_data
from models import Frequency, Observation, AggregationType
from src.client import CommunicationManager
from datetime import date

if __name__ == '__main__':
    cM = CommunicationManager()
    print(cM.get_version())

    data = generate_ts_data(2000,0,Frequency.MONTHLY,240)
    stats = cM.get_descriptive_statistics(data)
    print(stats)

    obs = [Observation(date=date(2022,1,1),value=1),
           Observation(date=date(2022,2,1),value=1),
           Observation(date=date(2022,3,1),value=1),
           Observation(date=date(2023,1,1),value=1),
           Observation(date=date(2023,2,1),value=1),
           Observation(date=date(2023,3,1),value=1),
           Observation(date=date(2023,4,1),value=1)]

    built = cM.build_ts_data(obs, aggregation_type=AggregationType.SUM, frequency=Frequency.YEARLY)
    print(built)

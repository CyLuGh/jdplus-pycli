from generator import generate_ts_data
from mapper import TsDataMapper
from models import Frequency, Observation, AggregationType, TsData, TsPeriod
from src.client import CommunicationManager
from datetime import date

if __name__ == '__main__':
    cM = CommunicationManager()
    print(cM.get_version())

    # data = generate_ts_data(2000,0,Frequency.MONTHLY,240)
    # stats = cM.get_descriptive_statistics(data)
    # print(stats)
    #
    # obs = [Observation(date=date(2022,1,1),value=1),
    #        Observation(date=date(2022,2,1),value=1),
    #        Observation(date=date(2022,3,1),value=1),
    #        Observation(date=date(2023,1,1),value=1),
    #        Observation(date=date(2023,2,1),value=1),
    #        Observation(date=date(2023,3,1),value=1),
    #        Observation(date=date(2023,4,1),value=1)]
    #
    # built = cM.build_ts_data(obs, aggregation_type=AggregationType.SUM, frequency=Frequency.YEARLY)
    # print(built)

    y = TsData( start= TsPeriod( year= 1977, position= 0, frequency= Frequency.YEARLY ),
                values=(500.0,510.0,525.0,520.0))
    disaggregated = cM.process_temporal_disaggregation(y,False, False, "Rw", 12, False, 0, False, 0, False, "SqrtDiffuse", False, 0, 6)

    print(disaggregated.stDevDisaggregatedSeries.get_date_values())
    print(disaggregated.as_dataframe())
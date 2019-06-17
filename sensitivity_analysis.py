from pathlib import Path
import main
from argparse import Namespace
from stroke import constants


if __name__ == '__main__':
    # change to data
    hospital_path = str(Path('data/hospitals/MA_n=100.csv'))
    times_path = str(Path('data/travel_times/MA_n=100.csv'))

    sex = constants.Sex.MALE
    age=70
    race=8
    time_since_symptoms=50
    s_default = 1000
    args = Namespace(
        patients=1,
        simulations=s_default,
        multicore=True,
        hospital_file=str(hospital_path),
        times_file=str(times_path),
        sex=sex,
        age=age,
        race=race,
        time_since_symptoms=time_since_symptoms)
    main.main_default_dtn(args)

    # upper = 1
    #
    # for age in range(70, 70 + upper, 5):  # 30 to 85
    #     for race in range(7, 7 + upper, 1):  # 0 to 9
    #         for time_since_symptoms in range(50, 100 + upper, 10):  # 10 to 100
    #             args = Namespace(
    #                 patients=1,
    #                 simulations=s_default,
    #                 multicore=True,
    #                 hospital_file=str(hospital_path),
    #                 times_file=str(times_path),
    #                 sex=sex,
    #                 age=age,
    #                 race=race,
    #                 time_since_symptoms=time_since_symptoms)
    #             main.main(args)

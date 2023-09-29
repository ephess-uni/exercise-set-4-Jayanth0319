""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    datestr_format = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(datestr, datestr_format)

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')

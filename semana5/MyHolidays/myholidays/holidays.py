from datetime import date
from datetime import datetime


class MyCalendar:
    def __init__(self, *args, **kwargs):
        self.datas = []
        self.datas.append(date(2021, 12, 5))
        self.datas.append(date(2021, 4, 21))

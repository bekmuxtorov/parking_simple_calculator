from datetime import datetime
from consts import Const


class FeesCalculator:
    def __init__(self):
        self.enterence_fee = Const.enterence_fee
        self.first_hour_fee = Const.first_hour_fee
        self.subsequent_hour_fee = Const.subsequent_hour_fee
        self.time_format = Const.time_format

    def str_to_datetime_object(self, time: str):
        try:
            return datetime.strptime(time, self.time_format)

        except ValueError:
            raise ValueError(
                f'Error entering time format: Enter {self.time_format} format')

    def calc(self, entered_time: str, left_time: str) -> int:
        cost = self.enterence_fee
        time_delta_secunds = (self.str_to_datetime_object(left_time) -
                              self.str_to_datetime_object(entered_time)).seconds

        if time_delta_secunds == 0:
            return cost

        if time_delta_secunds <= 3600:
            cost += self.first_hour_fee
            return cost
        else:
            cost += self.first_hour_fee
            cost += (time_delta_secunds // 3600 - 1) * self.subsequent_hour_fee
            if time_delta_secunds % 3600 != 0:
                cost += self.subsequent_hour_fee
            return cost

from datetime import date, datetime
from typing import Type

class HealthRecordFactory:

    def make_health_record(height: float, weight: float, gender, date_of_birth: date):
        # height in inches
        if height <= 0:
            raise TypeError
        # weight in pounds:
        if weight <= 0:
            raise TypeError
        # M or F
        allowed_genders = ['M','F']
        if gender not in allowed_genders:
            raise TypeError
        # any valid date string that can be parsed by python's datetime library - MM/DD/YYYY
        if datetime.strptime(date_of_birth, "%m/%d/%Y") is None:
            raise TypeError

        return HealthRecord(height, weight, gender, date_of_birth)


class HealthRecord:
    
    def __init__(self, height: float, weight: float, gender, date_of_birth: date):
        self.height = height  # height in inches
        self.weight = weight  # weight in pounds:
        self.gender = gender  # M or F
        self.date_of_birth = date_of_birth # expecting a python date

    def __str__(self) -> str:
        return f"h: {self.height} inches and w: {self.weight} pounds"

import pytest
from bmi.health_record import HealthRecord, HealthRecordFactory
from services.bmi_calc import *

@pytest.fixture
def health_rec() -> HealthRecord:
    return HealthRecordFactory.make_health_record(50, 150, 'M', 27)

def test_bmi_service_bmi_score():
    # arrange
    hr = HealthRecordFactory.make_health_record(15, 15, "M", 27)
    print(hr)
    # act
    score = bmi_score(hr.height, hr.weight, hr.gender, hr.age)

    # assert
    assert score > 0
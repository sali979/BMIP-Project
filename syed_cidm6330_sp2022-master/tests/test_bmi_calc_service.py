import pytest
from bmi.health_record import HealthRecord, HealthRecordFactory
from services.bmi_calc import bmi_score

@pytest.fixture
def health_rec() -> HealthRecord:
    return HealthRecordFactory.make_health_record(50, 150, 'F', '01/01/1980')

def test_bmi_service_bmi_score():
    # arrange
    hr = HealthRecordFactory.make_health_record(15, 15, "F", "01/01/1980")
    print(hr)
    # act
    score = bmi_score(hr.height, hr.weight)

    # assert
    assert score > 0
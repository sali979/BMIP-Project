from bmi.health_record import HealthRecord, HealthRecordFactory

def test_can_create_valid_health_record():
    # arrange
    hr = HealthRecordFactory.make_health_record(50, 50, "M", "01/01/1980")
    # act 
    # assert
    assert isinstance(hr, HealthRecord)
